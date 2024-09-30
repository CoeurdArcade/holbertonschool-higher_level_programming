#!/usr/bin/python3

# Import the write_file function from the module named '1-write_file'
from write_file import write_file

try:
    # Define the file name and the content to be written
    file_name = "my_first_file.txt"
    content = "This School is so cool!\n"

    # Call the write_file function to write the content to the file
    # The function returns the number of characters written to the file
    characters_written = write_file(file_name, content)

    # Print the number of characters written to the file
    print(f"Number of characters written: {characters_written}")

except Exception as e:
    # Print an error message if something goes wrong
    print(f"An error occurred: {e}")

