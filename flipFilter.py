import json

def filter_flips(data, min_profit_percentage, max_price, minimum_profit):
    filtered_flips = []

    for item_name, details in data.items():
        percentage_profit = details['percentage_profit']
        profit = details['profit']
        starting_bid = details['starting_bid']

        # Check if the flip meets the minimum profit percentage and is below the max price
        if (percentage_profit >= min_profit_percentage) and (starting_bid <= max_price) and (profit >= minimum_profit):
            #print(f"Item: {item_name}, Percentage Profit: {percentage_profit}, Starting Bid: {starting_bid}, Command: {details['command']}")
            filtered_flips.append({
                'item_name': item_name,
                'profit': profit,
                'percentage_profit': percentage_profit,
                'starting_bid': starting_bid,
                'estimated_price': details['estimated_price'],
                'command': details['command'],
                'api_call': details['api_call']
            })

    return filtered_flips

def filtrer_flips(min_profit_percentage, max_price, minimum_profit):
    # Load sorted flips with command data
    with open('percentage_difference_sorted_with_command.json', 'r') as file:
        sorted_flips = json.load(file)

    # Filter flips
    qualified_flips = filter_flips(sorted_flips, min_profit_percentage, max_price, minimum_profit)

    # Save filtered flips to a new JSON file
    with open('qualified_flips.json', 'w') as output_file:
        json.dump(qualified_flips, output_file, indent=4)

if __name__ == "__main__":
    filtrer_flips(30, 30*1000*1000, 300*1000)
