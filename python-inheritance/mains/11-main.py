#!/usr/bin/python3

# Import the Square class from the '11-square' module
Square = __import__('11-square').Square

# Create an instance of the Square class with a side length of 13
s = Square(13)

# Print the instance of the Square class
print(s)

# Print the area of the square by calling the area() method
print(s.area())

