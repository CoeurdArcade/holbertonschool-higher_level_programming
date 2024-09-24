#!/usr/bin/python3

# Import the BaseGeometry class from the '6-base_geometry' module
BaseGeometry = __import__('6-base_geometry').BaseGeometry

# Create an instance of the BaseGeometry class
bg = BaseGeometry()

try:
    # Attempt to call the 'area' method on the 'bg' instance
    print(bg.area())
except Exception as e:
    # Catch any exceptions raised by the 'area' method call
    # Print the exception type and message
    print("[{}] {}".format(e.__class__.__name__, e))

