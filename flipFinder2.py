import json
import requests


def calculate_profit(new_starting_bid, median_value):
    return  median_value - new_starting_bid


def calculate_profit_percentage(new_starting_bid, median_value):
    return (median_value - new_starting_bid)/new_starting_bid * 100

def main():
    # Load current raw data
    with open('current_raw_output_data.json', 'r') as file:
        current_data = json.load(file)

    # Initialize result dictionary
    result = {}

    # Calculate percentage differences
    for item in current_data:
        item_name = item['item_name']
        uuid = item['uuid']
        starting_bid = item['starting_bid']
        
        try:
            uuidResponse = requests.get(f"https://sky.coflnet.com/api/auction/{uuid}").json()
        except:
            print("Failed to get uuidResponse: " + uuid)
            pass
        
        
        tag = uuidResponse.get("tag")

        try:
            priceResponse = requests.get(f"https://sky.coflnet.com/api/item/price/{tag}/bin").json()
        except:
            print("Failed to get priceResponse: " + tag)
            continue
        
        try:
            estimated_price = (priceResponse.get("lowest")+priceResponse.get("secondLowest"))/2
        except:
            print(estimated_price)
            continue
        
        

        if estimated_price is not None:
            difference = calculate_profit(starting_bid, estimated_price)
            profit_percentage = calculate_profit_percentage(starting_bid, estimated_price)
            result[item_name] = {
                'profit': difference,
                'percentage_profit': profit_percentage,
                'starting_bid': starting_bid,
                'estimated_price': estimated_price,
                'command': f"/viewauction {item['uuid']}",
                'api_call': f"https://sky.coflnet.com/api/item/price/{tag}"
            }
 
    # Sort results by percentage difference in descending order
    sorted_result = dict(sorted(result.items(), key=lambda item: item[1]['percentage_profit'], reverse=True))

    # Save sorted results to a new JSON file
    with open('percentage_difference_sorted_with_command.json', 'w') as output_file:
        json.dump(sorted_result, output_file, indent=4)

if __name__ == "__main__":
    main()
