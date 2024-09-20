#!/usr/bin/python3

from typing import Type

# Import the Rectangle class from the '9-rectangle' module
Rectangle = __import__('9-rectangle').Rectangle

def main() -> None:
    try:
        # Create a square with side length 5 using the Rectangle.square method
        my_square: Type[Rectangle] = Rectangle.square(5)

        # Print the area and perimeter of the square
        print(f"Area: {my_square.area()} - Perimeter: {my_square.perimeter()}")

        # Print the square object (assuming it has a __str__ method for a readable representation)
        print(my_square)
    except Exception as e:
        # Catch any exceptions and print an error message
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()

