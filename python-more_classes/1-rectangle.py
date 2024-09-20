#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        # Initialize the width and height of the rectangle using the setter methods
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        # Return the private attribute __width
        return self.__width

    @width.setter
    def width(self, value):
        # Check if the value is an integer
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        # Check if the value is non-negative
        if value < 0:
            raise ValueError("width must be >= 0")
        # Set the private attribute __width
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        # Return the private attribute __height
        return self.__height

    @height.setter
    def height(self, value):
        # Check if the value is an integer
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        # Check if the value is non-negative
        if value < 0:
            raise ValueError("height must be >= 0")
        # Set the private attribute __height
        self.__height = value

