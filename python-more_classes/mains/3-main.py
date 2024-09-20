#!/usr/bin/python3

# Import the Rectangle class from the '3-rectangle' module
Rectangle = __import__('3-rectangle').Rectangle

# Create an instance of the Rectangle class with width 2 and height 4
my_rectangle = Rectangle(2, 4)

# Print the area and perimeter of the rectangle using the area() and perimeter() methods
print(f"Area: {my_rectangle.area()} - Perimeter: {my_rectangle.perimeter()}")

# Print the string representation of the rectangle using the str() method
print(str(my_rectangle))

# Print the official string representation of the rectangle using the repr() method
print(repr(my_rectangle))

# Print a separator line
print("--")

# Modify the width and height of the rectangle
my_rectangle.width = 10
my_rectangle.height = 3

# Print the updated string representation of the rectangle
print(my_rectangle)

# Print the updated official string representation of the rectangle
print(repr(my_rectangle))

