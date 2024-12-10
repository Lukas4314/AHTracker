import json

# File paths
new_data_file = "current_raw_output_data.json"
database_file = "auctions_database.json"

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist

def save_json(data, file_path):
    """Save JSON data to a file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def merge_and_sort_database(new_data, database):
    """Merge new data into the database based on uuid and timestamp, and sort by item_name."""
    # Convert the database to a dictionary keyed by UUID
    database_dict = {entry["uuid"]: entry for entry in database}
    
    # Process new data
    for entry in new_data:
        uuid = entry["uuid"]
        start_time = entry.get("start", 0)  # Default to 0 if start time is missing
        
        if uuid in database_dict:
            # Replace the record if the new one has a more recent start time
            if start_time > database_dict[uuid].get("start", 0):
                database_dict[uuid] = entry
        else:
            # Add new entries
            database_dict[uuid] = entry
    
    # Convert back to a list and sort by item_name
    merged_database = list(database_dict.values())
    merged_database.sort(key=lambda x: x.get("item_name", "").lower())
    
    return merged_database


def main():
    # Load the new data and the existing database
    new_data = load_json(new_data_file)
    database = load_json(database_file)

    # Merge and sort the database
    updated_database = merge_and_sort_database(new_data, database)

    # Save the updated database
    save_json(updated_database, database_file)

    print(f"Updated database saved to {database_file}")


if __name__ == "__main__":
    main()