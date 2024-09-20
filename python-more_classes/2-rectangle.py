#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width: int = 0, height: int = 0) -> None:
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle. Defaults to 0.
            height (int): The height of the new rectangle. Defaults to 0.
        """
        self.width = width  # Initialize width using the property setter
        self.height = height  # Initialize height using the property setter

    @property
    def width(self) -> int:
        """Get the width of the Rectangle."""
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        """Set the width of the Rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value  # Set the private attribute _width

    @property
    def height(self) -> int:
        """Get the height of the Rectangle."""
        return self._height

    @height.setter
    def height(self, value: int) -> None:
        """Set the height of the Rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value  # Set the private attribute _height

    def calculate_area(self) -> int:
        """Calculate and return the area of the Rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self._width * self._height  # Calculate area as width * height

    def calculate_perimeter(self) -> int:
        """Calculate and return the perimeter of the Rectangle.

        Returns:
            int: The perimeter of the rectangle. If width or height is 0, returns 0.
        """
        if self._width == 0 or self._height == 0:
            return 0  # Return 0 if width or height is 0
        return 2 * (self._width + self._height)  # Calculate perimeter as 2 * (width + height)

