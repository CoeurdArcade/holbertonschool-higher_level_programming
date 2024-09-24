#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""

# Import the Rectangle class from the module '9-rectangle'
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        # Validate that the size is an integer and greater than 0
        self.integer_validator("size", size)

        # Initialize the Rectangle class with equal width and height (since it's a square)
        super().__init__(size, size)

        # Store the size of the square
        self.__size = size

