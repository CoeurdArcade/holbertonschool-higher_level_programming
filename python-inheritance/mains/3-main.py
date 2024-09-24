#!/usr/bin/python3

# Import the is_kind_of_class function from the module '3-is_kind_of_class'
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

# Define a variable 'a' with an integer value
a = 1

# Check if 'a' is an instance of the 'int' class
if is_kind_of_class(a, int):
    # Print the type of 'a' if it is an instance of 'int'
    print("{} comes from {}".format(a, int.__name__))

# Check if 'a' is an instance of the 'float' class
if is_kind_of_class(a, float):
    # Print the type of 'a' if it is an instance of 'float'
    print("{} comes from {}".format(a, float.__name__))

# Check if 'a' is an instance of the 'object' class
if is_kind_of_class(a, object):
    # Print the type of 'a' if it is an instance of 'object'
    print("{} comes from {}".format(a, object.__name__))

