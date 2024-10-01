#!/usr/bin/env python3
"""
Creation of a module for serialization
of a dictionary into a JSON file.
"""
import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes the given data (assumed to be a dictionary) and saves it to a file.

    Parameters:
    data (dict): The data to be serialized.
    filename (str): The name of the file where the data will be saved.
    """
    try:
        # Open the file in write mode with UTF-8 encoding
        with open(filename, "w", encoding="utf-8") as outfile:
            # Serialize the data and write it to the file
            json.dump(data, outfile)
    except IOError as e:
        # Handle any I/O errors that occur during file operations
        print(f"Error writing to file {filename}: {e}")

def load_and_deserialize(filename):
    """
    Loads the data from a JSON file and deserializes it.

    Parameters:
    filename (str): The name of the file from which the data will be loaded.

    Returns:
    dict: The deserialized data.
    """
    try:
        # Open the file in read mode with UTF-8 encoding
        with open(filename, "r", encoding="utf-8") as infile:
            # Load the data from the file and deserialize it
            return json.load(infile)
    except IOError as e:
        # Handle any I/O errors that occur during file operations
        print(f"Error reading from file {filename}: {e}")
    except json.JSONDecodeError as e:
        # Handle any JSON decoding errors that occur during deserialization
        print(f"Error decoding JSON from file {filename}: {e}")


