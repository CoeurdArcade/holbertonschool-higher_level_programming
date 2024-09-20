#!/usr/bin/python3

# Import the Rectangle class from the '1-rectangle' module
Rectangle = __import__('1-rectangle').Rectangle

# Create a Rectangle instance with width 2 and height 4
my_rectangle = Rectangle(2, 4)

# Print the instance's dictionary
print(vars(my_rectangle))

# Update the width and height of the rectangle
my_rectangle.width = 10
my_rectangle.height = 3

# Print the updated instance's dictionary
print(vars(my_rectangle))

