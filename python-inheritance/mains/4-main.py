#!/usr/bin/python3

# Import the inherits_from function from the '4-inherits_from' module
inherits_from = __import__('4-inherits_from').inherits_from

# Define a variable 'a' with a boolean value True
a = True

# Check if 'a' inherits from the 'int' class
if inherits_from(a, int):
    # Print a message indicating that 'a' inherits from the 'int' class
    print("{} inherited from class {}".format(a, int.__name__))

# Check if 'a' inherits from the 'bool' class
if inherits_from(a, bool):
    # Print a message indicating that 'a' inherits from the 'bool' class
    print("{} inherited from class {}".format(a, bool.__name__))

# Check if 'a' inherits from the 'object' class
if inherits_from(a, object):
    # Print a message indicating that 'a' inherits from the 'object' class
    print("{} inherited from class {}".format(a, object.__name__))

