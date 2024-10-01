#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""

def class_to_json(obj):
    """
    Return the dictionary representation of a simple data structure.

    This function takes an object and returns its dictionary representation.
    It is particularly useful for converting instances of a class to a JSON-serializable format.

    Args:
        obj: An instance of a class with a __dict__ attribute.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__

