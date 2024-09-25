#!/usr/bin/env python3

import math
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Shape(ABC):
    """
    Abstract base class for shapes.
    """

    @abstractmethod
    def area(self) -> float:
        """
        Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """
        Calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass

class Circle(Shape):
    """
    A class representing a circle.
    """

    def __init__(self, radius: float):
        """
        Initialize a Circle object with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self) -> float:
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius

class Rectangle(Shape):
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
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.height * self.width

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.height + self.width)

def shape_info(shape: Shape) -> None:
    """
    Log the area and perimeter of a shape.

    Args:
        shape (Shape): The shape object.
    """
    logging.info(f"Area: {shape.area()}")
    logging.info(f"Perimeter: {shape.perimeter()}")

def main():
    """
    Main function to create shapes and display their information.
    """
    try:
        circle = Circle(radius=5)
        rectangle = Rectangle(width=4, height=7)

        shape_info(circle)
        shape_info(rectangle)
    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

