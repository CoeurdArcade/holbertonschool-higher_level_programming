#!/usr/bin/python3
"""
Defines an object attribute lookup function.

This module contains a function that returns a list of an object's available attributes.
"""

def lookup(obj):
    """
    Return a list of an object's available attributes.

    This function takes an object as input and returns a list of its attributes.

    Args:
        obj: The object whose attributes are to be listed.

    Returns:
        list: A list of attribute names.
    """
    return (dir(obj))

