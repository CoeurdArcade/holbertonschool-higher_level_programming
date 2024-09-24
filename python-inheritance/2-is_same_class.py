#!/usr/bin/python3

# Import the is_same_class function from the '2-is_same_class' module
is_same_class = __import__('2-is_same_class').is_same_class

# Define a variable 'a' and assign it the value 1
a = 1

# Check if 'a' is an instance of the class 'int' using the is_same_class function
if is_same_class(a, int):
    # If true, print that 'a' is an instance of the class 'int'
    print("{} is an instance of the class {}".format(a, int.__name__))

# Check if 'a' is an instance of the class 'float' using the is_same_class function
if is_same_class(a, float):
    # If true, print that 'a' is an instance of the class 'float'
    print("{} is an instance of the class {}".format(a, float.__name__))

# Check if 'a' is an instance of the class 'object' using the is_same_class function
if is_same_class(a, object):
    # If true, print that 'a' is an instance of the class 'object'
    print("{} is an instance of the class {}".format(a, object.__name__))

