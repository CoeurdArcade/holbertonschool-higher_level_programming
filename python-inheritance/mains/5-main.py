#!/usr/bin/python3

# Import the BaseGeometry class from the '5-base_geometry' module
BaseGeometry = __import__('5-base_geometry').BaseGeometry

# Create an instance of the BaseGeometry class
bg = BaseGeometry()

# Print the instance of BaseGeometry
print(bg)

# Print the list of attributes and methods of the instance 'bg'
print(dir(bg))

# Print the list of attributes and methods of the BaseGeometry class
print(dir(BaseGeometry))

