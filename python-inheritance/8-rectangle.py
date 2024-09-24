#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

# Import the BaseGeometry class from the '7-base_geometry' module
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        # Validate the width using the integer_validator method from BaseGeometry
        self.integer_validator("width", width)
        # Set the private attribute __width
        self.__width = width
        # Validate the height using the integer_validator method from BaseGeometry
        self.integer_validator("height", height)
        # Set the private attribute __height
        self.__height = height

