#!/usr/bin/python3

# Import the Square class from the module '1-square'
from Square import Square

# Create an instance of the Square class with a size of 3
my_square = Square(3)

# Print the type of the instance
print(type(my_square))

# Print the instance's dictionary
print(my_square.__dict__)

# Attempt to print the 'size' attribute and handle any exceptions
try:
    print(my_square.size)
except AttributeError as e:
    print(f"AttributeError: {e}")

# Attempt to print the '__size' attribute and handle any exceptions
try:
    print(my_square.__size)
except AttributeError as e:
    print(f"AttributeError: {e}")

