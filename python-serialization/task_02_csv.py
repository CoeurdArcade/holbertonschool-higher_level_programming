#!/usr/bin/env python3
"""
Convert CSV data to JSON format.
"""
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to a JSON file.

    Parameters:
    csv_filename (str): The path to the CSV file.

    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Open the CSV file and read its contents
        with open(csv_filename, mode='r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = [row for row in csv_reader]

        # Convert the data to JSON format
        json_data = json.dumps(data_list, indent=4)

        # Write the JSON data to a file
        with open('data.json', mode='w') as json_file:
            json_file.write(json_data)

        return True
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
if __name__ == "__main__":
    csv_file = 'example.csv'  # Replace with your CSV file path
    success = convert_csv_to_json(csv_file)
    if success:
        print("Conversion successful!")
    else:
        print("Conversion failed.")

