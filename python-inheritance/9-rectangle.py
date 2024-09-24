#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

# Import the BaseGeometry class from the module '7-base_geometry'
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
        super().integer_validator("width", width)
        # Set the width as a private attribute
        self.__width = width
        # Validate the height using the integer_validator method from BaseGeometry
        super().integer_validator("height", height)
        # Set the height as a private attribute
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        # Calculate and return the area of the rectangle
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        # Create a string representation of the Rectangle
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

