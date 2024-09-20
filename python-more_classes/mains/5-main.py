#!/usr/bin/python3

# Import the Rectangle class from the '5-rectangle' module
Rectangle = __import__('5-rectangle').Rectangle

# Create an instance of Rectangle with width 2 and height 4
my_rectangle = Rectangle(2, 4)

# Print the area and perimeter of the rectangle using f-strings for formatting
print(f"Area: {my_rectangle.area()} - Perimeter: {my_rectangle.perimeter()}")

# Delete the rectangle instance
del my_rectangle

# Try to print the deleted rectangle instance
try:
    print(my_rectangle)
# Catch the NameError exception that occurs when trying to access a deleted variable
except NameError as e:
    # Print the exception type and message using f-strings for formatting
    print(f"[{e.__class__.__name__}] {e}")

