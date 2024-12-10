import json
from collections import defaultdict

# File paths
database_file = "auctions_database.json"
output_file = "average_lowest_bins_averge.json"

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_json(data, file_path):
    """Save JSON data to a file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def calculate_average_lowest_bins(database):
    """Calculate the average of the lowest BIN prices for each unique item."""
    item_bins = defaultdict(list)

    # Organize BIN prices by item
    for entry in database:
        item_name = entry["item_name"]
        starting_bid = entry["starting_bid"]
        item_bins[item_name].append(starting_bid)

    # Calculate the average of the lowest 3 BIN prices for each item
    average_bins = {}
    for item_name, bins in item_bins.items():
        bins.sort()  # Sort the BIN prices
        if len(bins) >= 3:
            lowest_3_bins = bins[:3]
            average_bin = sum(lowest_3_bins) / len(lowest_3_bins)
            average_bins[item_name] = average_bin
        if len(bins) == 2:
            average_bins[item_name] = sum(bins) / len(bins)
        if len(bins) == 1:
            average_bins[item_name] = bins[0]

    return average_bins


def main():
    # Load the database
    database = load_json(database_file)

    # Calculate the averages of the lowest BIN prices
    average_bins = calculate_average_lowest_bins(database)

    # Save the new JSON file with the calculated averages
    save_json(average_bins, output_file)

    print(f"Averages of the lowest BIN prices saved to {output_file}")


if __name__ == "__main__":
    main()
