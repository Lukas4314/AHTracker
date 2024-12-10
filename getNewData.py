import json
import requests
from datetime import datetime
import time
# File paths
current_raw_output_file = "current_raw_output_data.json"
base_api_url = "https://api.hypixel.net/v2/skyblock/auctions"
updateTimesFile = "updateTimes.json"


 
def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"auctions": [], "lastUpdated": None}

def save_json(data, file_path):
    """Save JSON data to a file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
        
# Function to fetch data from a single page
def fetch_page_data(page):
    response = requests.get(f"{base_api_url}?page={page}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch page {page}. Status code: {response.status_code}")
        return None

def update_raw_data():


    with open(updateTimesFile, 'r') as file:
        last_updated_data = json.load(file)
    
    try:
        last_updated = last_updated_data[-1]["lastUpdated"]
    except:
        last_updated = 0

    #print(last_updated)
    
    initial_response = fetch_page_data(0)

    if initial_response and initial_response.get("success"):
        total_pages = initial_response.get("totalPages", 0)
        #print(f"Total pages to fetch: {total_pages}")
        
        # Collect data from all pages
        all_auctions = []
        should_break = False
        for page in range(total_pages):
            if should_break:
                break
            #print(f"Fetching page {page}...")
            page_data = fetch_page_data(page)
            if page_data and page_data.get("auctions"):
                for auction in page_data["auctions"]:
            
                    if auction.get("start", 0) <= last_updated:
                        #print("Reached the last updated auction. Stopping...")
                        should_break = True
                        break
                    if auction.get("start", 0) == 0:
                        #print("Something is fucked up")
                        break
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
        
        #print(f"Data successfully saved to {output_file}")
    else:
        print("Failed to fetch initial page or invalid response.")
        
        
    # Append the new data
    try:
        last_updated_data.append({"lastUpdated": all_auctions[1]["start"]})
    except:
        #print("No new data to append")
        pass

    # Write the updated data back to the file
    with open(updateTimesFile, 'w') as file:
        json.dump(last_updated_data, file, indent=4)
        
