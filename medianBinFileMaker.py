import json
from collections import defaultdict

# File paths
database_file = "auctions_database.json"
output_file = "median_bin.json"

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

def calculate_median_bin(database):
    """Calculate the average of the lowest BIN prices for each unique item."""
    item_bins = defaultdict(list)

    # Organize BIN prices by item
    for entry in database:
        item_name = entry["item_name"]
        starting_bid = entry["starting_bid"]
        item_bins[item_name].append(starting_bid)

    # Calculate the average of the lowest 3 BIN prices for each item
    medianBins = {}
    for item_name, bins in item_bins.items():
        bins.sort()  # Sort the BIN prices
        if len(bins) >= 3:
            medianBins[item_name] =bins[len(bins)//2]
    return medianBins


def main():
    # Load the database
    database = load_json(database_file)

    # Calculate the averages of the lowest BIN prices
    median_bins = calculate_median_bin(database)

    # Save the new JSON file with the calculated averages
    save_json(median_bins, output_file)

    print(f"median of the lowest BIN prices saved to {output_file}")


if __name__ == "__main__":
    main()
