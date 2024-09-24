#!/usr/bin/python3

# Import the Rectangle class from the '9-rectangle' module
Rectangle = __import__('9-rectangle').Rectangle

# Create an instance of the Rectangle class with width 3 and height 5
r = Rectangle(3, 5)

# Print the string representation of the rectangle object
print(r)

# Print the area of the rectangle by calling the area() method
print(r.area())

