#!/usr/bin/python3
"""Defines a text file-reading function."""

def read_file(filename=""):
    """
    Print the contents of a UTF8 text file to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.
    """
    # Open the file with the specified filename in read mode with UTF-8 encoding
    with open(filename, encoding="utf-8") as f:
        # Read the entire contents of the file
        file_contents = f.read()
        # Print the contents of the file to the standard output (stdout)
        print(file_contents, end="")

