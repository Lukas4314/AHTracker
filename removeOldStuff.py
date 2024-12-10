import json
from datetime import datetime, timedelta

# File paths
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

def remove_old_entries(database, days_old=3):
    """Remove entries older than the specified number of days."""
    # Calculate the timestamp for 3 days ago
    cutoff_date = datetime.now() - timedelta(days=days_old)
    cutoff_timestamp = int(cutoff_date.timestamp() * 1000)  # Convert to milliseconds

    # Filter out old entries
    updated_database = [entry for entry in database if entry.get("start", 0) > cutoff_timestamp]

    return updated_database

# Load the database
database = load_json(database_file)

# Remove old entries (older than 3 days)
updated_database = remove_old_entries(database)

# Save the updated database
save_json(updated_database, database_file)

print(f"Updated database saved to {database_file}")
