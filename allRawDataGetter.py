import requests
import json

# Define the base API URL
base_api_url = "https://api.hypixel.net/v2/skyblock/auctions"


# Function to fetch data from a single page
def fetch_page_data(page):
    response = requests.get(f"{base_api_url}?page={page}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch page {page}. Status code: {response.status_code}")
        return None

# Fetch the first page to determine the total pages
initial_response = fetch_page_data(0)

if initial_response and initial_response.get("success"):
    total_pages = initial_response.get("totalPages", 0)
    print(f"Total pages to fetch: {total_pages}")
    
    # Collect data from all pages
    all_auctions = []
    
    for page in range(total_pages):
        print(f"Fetching page {page}...")
        page_data = fetch_page_data(page)
        if page_data and page_data.get("auctions"):
            for auction in page_data["auctions"]:
                if auction.get("bin", False):
                    all_auctions.append({
                        "item_name": auction.get("item_name", "Unknown"),
                        "extra": auction.get("extra", "Unknown"),
                        "starting_bid": auction.get("starting_bid", 0),
                        "uuid": auction.get("uuid", "Unknown"),
                        "start": auction.get("start", 0),
                    })
    
    # Save all auction data to a JSON file
    output_file = "current_raw_output_data.json"
    with open(output_file, "w") as file:
        json.dump(all_auctions, file, indent=4)
    
    print(f"Data successfully saved to {output_file}")
else:
    print("Failed to fetch initial page or invalid response.")
