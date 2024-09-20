#!/usr/bin/python3

# Import the Rectangle class from the '4-rectangle' module
Rectangle = __import__('4-rectangle').Rectangle

# Create an instance of Rectangle with width 2 and height 4
my_rectangle = Rectangle(2, 4)

# Print the string representation of the rectangle
print(f"str(my_rectangle): {str(my_rectangle)}")

# Print the default representation of the rectangle
print(f"my_rectangle: {my_rectangle}")

# Print the official string representation of the rectangle
print(f"repr(my_rectangle): {repr(my_rectangle)}")

# Print the hexadecimal memory address of the rectangle instance
print(f"hex(id(my_rectangle)): {hex(id(my_rectangle))}")

# Create a new instance of Rectangle based on the representation of the original rectangle
new_rectangle = eval(repr(my_rectangle))

# Print the string representation of the new rectangle
print(f"str(new_rectangle): {str(new_rectangle)}")

# Print the default representation of the new rectangle
print(f"new_rectangle: {new_rectangle}")

# Print the official string representation of the new rectangle
print(f"repr(new_rectangle): {repr(new_rectangle)}")

# Print the hexadecimal memory address of the new rectangle instance
print(f"hex(id(new_rectangle)): {hex(id(new_rectangle))}")

# Check if the new rectangle is the same instance as the original rectangle
print(f"new_rectangle is my_rectangle: {new_rectangle is my_rectangle}")

# Check if the type of the new rectangle is the same as the type of the original rectangle
print(f"type(new_rectangle) is type(my_rectangle): {type(new_rectangle) is type(my_rectangle)}")

