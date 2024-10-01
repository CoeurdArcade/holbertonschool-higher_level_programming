#!/usr/bin/python3

# Import the save_to_json_file function from the '5-save_to_json_file' module
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

# Define the filename for the JSON file
filename = "my_list.json"

# Define a list to be saved as JSON
my_list = [1, 2, 3]

# Save the list to a JSON file
save_to_json_file(my_list, filename)

# Define the filename for the JSON file
filename = "my_dict.json"

# Define a dictionary to be saved as JSON
my_dict = {
        'id': 12,
        'name': "John",
        'places': [ "San Francisco", "Tokyo" ],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
            }
        }

# Save the dictionary to a JSON file
save_to_json_file(my_dict, filename)

# Try to save a set to a JSON file, which is not JSON serializable
try:
    # Define the filename for the JSON file
    filename = "my_set.json"

    # Define a set to be saved as JSON (this will raise an exception)
    my_set = { 132, 3 }

    # Attempt to save the set to a JSON file
    save_to_json_file(my_set, filename)

# Catch any exceptions that occur during the save operation
except Exception as e:
    # Print the exception type and message
    print("[{}] {}".format(e.__class__.__name__, e))

