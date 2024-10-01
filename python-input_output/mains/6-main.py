#!/usr/bin/python3

# Import the load_from_json_file function from the '6-load_from_json_file' module
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def load_and_print_json(filename):
    """
    Load a JSON file and print its content and type.
    Handle and print exceptions if any occur.
    """
    try:
        data = load_from_json_file(filename)
        print(data)
        print(type(data))
    except FileNotFoundError:
        print(f"[FileNotFoundError] The file '{filename}' does not exist.")
    except json.JSONDecodeError:
        print(f"[JSONDecodeError] The file '{filename}' is not a valid JSON file.")
    except Exception as e:
        print(f"[{e.__class__.__name__}] {e}")

# Define filenames for the JSON files
list_filename = "my_list.json"
dict_filename = "my_dict.json"
non_existent_filename = "my_set_doesnt_exist.json"
fake_filename = "my_fake.json"

# Load and print the JSON files
load_and_print_json(list_filename)
load_and_print_json(dict_filename)
load_and_print_json(non_existent_filename)
load_and_print_json(fake_filename)

