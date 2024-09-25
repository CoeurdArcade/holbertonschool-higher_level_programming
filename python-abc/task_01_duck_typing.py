# task_01_duck_typing.py

from typing import Protocol

class Shape(Protocol):
    """
    Protocol for shapes that have an area and perimeter.
    """
    def area(self) -> float:
        """
        Calculate the area of the shape.
        """
        ...

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the shape.
        """
        ...

class Circle:
    """
    A class representing a circle.
    """
    def __init__(self, radius: float):
        """
        Initialize a Circle object with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self) -> float:
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return 3.14159 * self.radius ** 2

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * 3.14159 * self.radius

class Rectangle:
    """
    A class representing a rectangle.
    """
    def __init__(self, width: float, height: float):
        """
        Initialize a Rectangle object with a given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

def shape_info(shape: Shape) -> None:
    """
    Print the area and perimeter of a shape.

    Args:
        shape (Shape): The shape object.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

