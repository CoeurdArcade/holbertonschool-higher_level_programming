#!/usr/bin/python3

# Import the BaseGeometry class from the '7-base_geometry' module
BaseGeometry = __import__('7-base_geometry').BaseGeometry

# Create an instance of the BaseGeometry class
bg = BaseGeometry()

# Validate an integer with the name "my_int" and value 12
bg.integer_validator("my_int", 12)

# Validate an integer with the name "width" and value 89
bg.integer_validator("width", 89)

# Attempt to validate a non-integer value with the name "name" and value "John"
# This should raise an exception
try:
    bg.integer_validator("name", "John")
except Exception as e:
    # Print the exception type and message
    print("[{}] {}".format(e.__class__.__name__, e))

# Attempt to validate an integer with the name "age" and value 0
# This should raise an exception if 0 is not a valid value
try:
    bg.integer_validator("age", 0)
except Exception as e:
    # Print the exception type and message
    print("[{}] {}".format(e.__class__.__name__, e))

# Attempt to validate an integer with the name "distance" and value -4
# This should raise an exception if negative values are not valid
try:
    bg.integer_validator("distance", -4)
except Exception as e:
    # Print the exception type and message
    print("[{}] {}".format(e.__class__.__name__, e))

