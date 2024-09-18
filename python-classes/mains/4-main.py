#!/usr/bin/python3

# Import the Square class from the '4-square' module
Square = __import__('4-square').Square

# Create an instance of Square with size 89
my_square = Square(89)

# Print the area and size of the square
print(f"Area: {my_square.area()} for size: {my_square.size}")

# Change the size of the square to 3
my_square.size = 3

# Print the area and size of the square after changing the size
print(f"Area: {my_square.area()} for size: {my_square.size}")

# Try to set the size to an invalid value and handle the exception
try:
    my_square.size = "5 feet"
    print(f"Area: {my_square.area()} for size: {my_square.size}")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

