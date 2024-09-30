#!/usr/bin/python3

"""
This script demonstrates the conversion of Python data structures to JSON strings
using the to_json_string function from the '3-to_json_string' module.
"""

# Import the to_json_string function from the '3-to_json_string' module
to_json_string = __import__('3-to_json_string').to_json_string

def convert_and_print(data, data_name):
    """
    Convert the given data to a JSON string and print the result along with its type.

    Args:
        data: The data to be converted to a JSON string.
        data_name (str): The name of the data for display purposes.
    """
    try:
        json_string = to_json_string(data)
        print(f"{data_name} as JSON string: {json_string}")
        print(f"Type of {data_name} JSON string: {type(json_string)}")
    except Exception as e:
        print(f"[{e.__class__.__name__}] {e} - Error converting {data_name} to JSON string")

# Define a list
my_list = [1, 2, 3]
convert_and_print(my_list, "my_list")

# Define a dictionary with various data types
my_dict = {
        'id': 12,
        'name': "John",
        'places': ["San Francisco", "Tokyo"],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
            }
        }
convert_and_print(my_dict, "my_dict")

# Define a set
my_set = {132, 3}
convert_and_print(my_set, "my_set")

