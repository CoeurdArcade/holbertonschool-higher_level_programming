#!/usr/bin/python3
"""Defines a string-to-JSON function."""

# Import the json module which provides methods for working with JSON data
import json

def to_json_string(my_obj):
    """
    Return the JSON representation of a string object.

    This function takes an object (my_obj) and converts it to a JSON formatted string.

    Args:
        my_obj: The object to be converted to a JSON string.

    Returns:
        A JSON formatted string representing the input object.
    """
    # Use json.dumps() to convert the input object to a JSON formatted string
    return json.dumps(my_obj)

