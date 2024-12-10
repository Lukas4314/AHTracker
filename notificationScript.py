import json
from plyer import notification
import os

def check_and_update_json(input_file, output_file):
    try:
        # Read input JSON file
        with open(input_file, 'r') as infile:
            input_data = json.load(infile)
        
        # Ensure the output file exists or create it
        if os.path.exists(output_file):
            with open(output_file, 'r') as outfile:
                try:
                    existing_data = json.load(outfile)
                except json.JSONDecodeError:
                    existing_data = []
        else:
            existing_data = []

        # Check for duplicates
        existing_commands = {entry["command"] for entry in existing_data}
        new_entries = [entry for entry in input_data if entry["command"] not in existing_commands]

        if new_entries:
            # Write new entries to the output file (prepend new entries to the existing data)
            with open(output_file, 'w') as outfile:
                json.dump(new_entries + existing_data, outfile, indent=4)
            
            # Display a notification
            notification.notify(
                title="New Items Found",
                message=f"{len(new_entries)} new items added to {output_file}.",
                timeout=5  # Notification lasts 5 seconds
            )
            print(f"{len(new_entries)} new items added to {output_file}.")
        else:
            print("No new items found. No update made.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the input file.")


def main():
    # Define input and output file paths
    input_file = "qualified_flips.json"  # Replace with your input JSON file path
    output_file = "1flips.json"  # Replace with your output JSON file path

    check_and_update_json(input_file, output_file)
if __name__ == "__main__":
    main()