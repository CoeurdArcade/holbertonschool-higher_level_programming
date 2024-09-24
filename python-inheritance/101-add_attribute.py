#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""

def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    # Check if the object has a __dict__ attribute, which indicates it can have new attributes added
    if not hasattr(obj, "__dict__"):
        # Raise a TypeError if the object cannot have new attributes added
        raise TypeError("can't add new attribute")
    # Use setattr to add the new attribute to the object
    setattr(obj, att, value)

