#!/usr/bin/python3
"""Defines a JSON file-writing function."""

# Import the json module to work with JSON data
import json

def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.

    Args:
    my_obj: The object to be written to the file.
    filename: The name of the file where the JSON representation will be saved.
    """

    # Open the file in write mode
    with open(filename, "w") as f:
        # Use json.dump to serialize the object and write it to the file
        json.dump(my_obj, f)

