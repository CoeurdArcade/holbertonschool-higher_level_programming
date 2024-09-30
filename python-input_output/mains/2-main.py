#!/usr/bin/python3

# Import the append_write function from the '2-append_write' module
from append_write import append_write

# Define constants for the file name and the text to be appended
FILE_NAME = "file_append.txt"
TEXT_TO_APPEND = "This School is so cool!\n"

try:
    # Call the append_write function to append the text to the file
    # The function returns the number of characters added to the file
    nb_characters_added = append_write(FILE_NAME, TEXT_TO_APPEND)

    # Print the number of characters added to the file
    print(nb_characters_added)

except FileNotFoundError:
    print(f"Error: The file '{FILE_NAME}' was not found.")
except PermissionError:
    print(f"Error: Permission denied when trying to write to '{FILE_NAME}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

