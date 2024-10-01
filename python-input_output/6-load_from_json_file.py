#!/usr/bin/python3
"""
Defines a JSON file-reading function.
"""

# Import the json module to work with JSON data
import json

def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        The Python object created from the JSON file.
    """

    # Open the file in read mode
    with open(filename) as f:
        # Use json.load to parse the JSON file and return the resulting Python object
        return json.load(f)

