#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a JSON-to-object function."""

# Import the json module, which provides functions for working with JSON data
import json

def from_json_string(my_str):
    """
    Return the Python object representation of a JSON string.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        The Python object representation of the JSON string.
    """
    # Use the json.loads() function to parse the JSON string and convert it to a Python object
    return json.loads(my_str)

