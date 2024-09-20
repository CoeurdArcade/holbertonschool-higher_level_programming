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
        self.width = width  # Initialize width with validation
        self.height = height  # Initialize height with validation

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        self.__validate_dimension(value, "width")  # Validate the width value
        self.__width = value  # Set the width if validation passes

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        self.__validate_dimension(value, "height")  # Validate the height value
        self.__height = value  # Set the height if validation passes

    def __validate_dimension(self, value, dimension_name):
        """Validate the dimension value.

        Args:
            value (int): The value to validate.
            dimension_name (str): The name of the dimension ('width' or 'height').

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{dimension_name} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension_name} must be >= 0")

# Example usage:
# rect = Rectangle(5, 10)
# print(rect.width)  # Output: 5
# print(rect.height)  # Output: 10
# rect.width = 7
# print(rect.width)  # Output: 7

