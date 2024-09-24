#!/usr/bin/python3

# Import the lookup function from the '0-lookup' module
lookup = __import__('0-lookup').lookup

# Define a class MyClass1 which inherits from the base 'object' class
class MyClass1(object):
    """A simple class with no attributes or methods."""
    pass

# Define a class MyClass2 which inherits from the base 'object' class
class MyClass2(object):
    """A class with a class attribute and a method."""
    my_attr1 = 3  # Class attribute

    def my_meth(self) -> None:
        """A method that does nothing."""
        pass

# Print the list of attributes and methods of MyClass1 using the lookup function
print(lookup(MyClass1))

# Print the list of attributes and methods of MyClass2 using the lookup function
print(lookup(MyClass2))

# Print the list of attributes and methods of the built-in 'int' type using the lookup function
print(lookup(int))

