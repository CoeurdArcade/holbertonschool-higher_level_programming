#!/usr/bin/python3

"""
This script demonstrates converting JSON strings to Python objects
using the from_json_string function from the '4-from_json_string' module.
"""

# Import the from_json_string function from the '4-from_json_string' module
from_json_string = __import__('4-from_json_string').from_json_string

def convert_and_print_json(json_string):
    """
    Convert a JSON string to a Python object and print the result.

    Args:
        json_string (str): The JSON string to convert.
    """
    try:
        # Convert the JSON string to a Python object
        python_object = from_json_string(json_string)

        # Print the converted object
        print(python_object)

        # Print the type of the converted object
        print(type(python_object))

    except Exception as e:
        # Print the exception type and message
        print(f"[{e.__class__.__name__}] {e}")

# Define JSON strings as constants
JSON_LIST_STRING = "[1, 2, 3]"
JSON_DICT_STRING = """
{
    "is_active": true,
    "info": {"age": 36, "average": 3.14},
    "id": 12,
    "name": "John",
    "places": ["San Francisco", "Tokyo"]
}
"""
INVALID_JSON_STRING = """
{
    "is_active": true, 12
}
"""

# Convert and print the JSON list string
print("Converting JSON list string:")
convert_and_print_json(JSON_LIST_STRING)

# Convert and print the JSON dictionary string
print("\nConverting JSON dictionary string:")
convert_and_print_json(JSON_DICT_STRING)

# Convert and print the invalid JSON string
print("\nConverting invalid JSON string:")
convert_and_print_json(INVALID_JSON_STRING)

