#!/usr/bin/python3
"""
Defines an inherited list class MyList.
This module contains a custom class MyList that inherits from the built-in list class.
"""

class MyList(list):
    """
    Implements sorted printing for the built-in list class.
    This class extends the functionality of the built-in list class by adding a method
    to print the list in sorted ascending order.
    """

    def print_sorted(self):
        """
        Print a list in sorted ascending order.
        This method sorts the list and prints the sorted version.
        """
        print(sorted(self))

