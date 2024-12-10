import json

def calculate_percentage_difference(new_starting_bid, median_value):
    return ((new_starting_bid - median_value) / median_value) * 100

def main():
    # Load current raw data
    with open('current_raw_output_data.json', 'r') as file:
        current_data = json.load(file)

    # Load median bin values
    with open('median_bin.json', 'r') as file:
        median_bin_data = json.load(file)

    # Initialize result dictionary
    result = {}

    # Calculate percentage differences
    for item in current_data:
        item_name = item['item_name']
        starting_bid = item['starting_bid']
        median_value = median_bin_data.get(item_name)

        if median_value is not None:
            difference = calculate_percentage_difference(starting_bid, median_value)
            result[item_name] = {
                'percentage_difference': difference,
                'command': f"/viewauction {item['uuid']}"
            }

    # Sort results by percentage difference in descending order
    sorted_result = dict(sorted(result.items(), key=lambda item: item[1]['percentage_difference'], reverse=True))

    # Save sorted results to a new JSON file
    with open('percentage_difference_sorted_with_command.json', 'w') as output_file:
        json.dump(sorted_result, output_file, indent=4)

if __name__ == "__main__":
    main()
