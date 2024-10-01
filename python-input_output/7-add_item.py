#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json

def load_from_json_file(filename):
    """Load a list from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_to_json_file(obj, filename):
    """Save a list to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(obj, file)

if __name__ == "__main__":
    # Load existing items from the file, or start with an empty list if the file doesn't exist
    items = load_from_json_file("add_item.json")

    # Extend the list with command-line arguments (excluding the script name)
    items.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file(items, "add_item.json")

