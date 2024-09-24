#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""

class MyInt(int):
    """Invert int operators == and !=.

    This class inherits from the built-in int class and overrides the equality
    (==) and inequality (!=) operators to invert their behavior.
    """

    def __eq__(self, value):
        """Override == operator with != behavior.

        This method is called when the == operator is used. Instead of checking
        for equality, it checks for inequality.

        Args:
            value: The value to compare against.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior.

        This method is called when the != operator is used. Instead of checking
        for inequality, it checks for equality.

        Args:
            value: The value to compare against.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return self.real == value

