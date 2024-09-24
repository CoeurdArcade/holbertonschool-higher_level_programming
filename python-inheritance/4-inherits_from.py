#!/usr/bin/python3
"""Defines an inherited class-checking function."""

def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if obj is an inherited instance of a_class, False otherwise.
    """
    # Check if the type of obj is a subclass of a_class and is not exactly a_class itself
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

