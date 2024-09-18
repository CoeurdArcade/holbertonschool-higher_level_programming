#!/usr/bin/python3

# Import the Square class from the '101-square' module
Square = __import__('101-square').Square

# Create a Square object with size 5 and position (0, 0)
square1 = Square(5, (0, 0))
print(square1)

print("--")

# Create another Square object with size 5 and position (4, 1)
square2 = Square(5, (4, 1))
print(square2)

