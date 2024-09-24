#!/usr/bin/python3

# Import the Rectangle class from the '8-rectangle' module
Rectangle = __import__('8-rectangle').Rectangle

# Create an instance of Rectangle with width 3 and height 5
r = Rectangle(3, 5)

# Print the string representation of the rectangle instance
print(r)

# Print the list of attributes and methods of the rectangle instance
print(dir(r))

# Try to print the width and height of the rectangle
try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    # If an exception occurs, print the exception type and message
    print("[{}] {}".format(e.__class__.__name__, e))

# Try to create a new rectangle with invalid dimensions (width 4 and height True)
try:
    r2 = Rectangle(4, True)
except Exception as e:
    # If an exception occurs, print the exception type and message
    print("[{}] {}".format(e.__class__.__name__, e))

