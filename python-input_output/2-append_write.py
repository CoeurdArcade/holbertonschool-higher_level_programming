#!/usr/bin/python3
"""Defines a file-appending function."""

def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    # Open the file in append mode with UTF-8 encoding
    with open(filename, "a", encoding="utf-8") as f:
        # Write the text to the file and return the number of characters written
        return f.write(text)

