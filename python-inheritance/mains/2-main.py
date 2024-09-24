#!/usr/bin/python3

# Import the is_same_class function from the '2-is_same_class' module
is_same_class = __import__('2-is_same_class').is_same_class

# Initialize a variable 'a' with an integer value
a = 1

# Check if 'a' is an instance of the class 'int'
if is_same_class(a, int):
    # Print the result if 'a' is an instance of the class 'int'
    print("{} is an instance of the class {}".format(a, int.__name__))

# Check if 'a' is an instance of the class 'float'
if is_same_class(a, float):
    # Print the result if 'a' is an instance of the class 'float'
    print("{} is an instance of the class {}".format(a, float.__name__))

# Check if 'a' is an instance of the class 'object'
if is_same_class(a, object):
    # Print the result if 'a' is an instance of the class 'object'
    print("{} is an instance of the class {}".format(a, object.__name__))

