#!/usr/bin/python3
"""Defines a file-writing function."""

def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    # Open the file in write mode with UTF-8 encoding
    with open(filename, "w", encoding="utf-8") as f:
        # Write the text to the file and return the number of characters written
        return f.write(text)

