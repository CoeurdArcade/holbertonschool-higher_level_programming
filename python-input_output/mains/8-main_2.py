#!/usr/bin/python3

"""
This script demonstrates the use of MyClass and the class_to_json function.
It creates an instance of MyClass, calls a method on it, and then converts
the instance to a JSON-serializable dictionary.
"""

# Import the MyClass from the module '8-my_class_2'
from my_class_2 import MyClass

# Import the class_to_json function from the module '8-class_to_json'
from class_to_json import class_to_json

# Create an instance of MyClass with the name "John"
my_instance = MyClass("John")

# Call the win method on the instance my_instance
my_instance.win()

# Print the type of the instance my_instance
print(type(my_instance))

# Print the instance my_instance (this will call the __str__ method of MyClass)
print(my_instance)

# Convert the instance my_instance to a JSON-serializable dictionary using the class_to_json function
json_serializable_dict = class_to_json(my_instance)

# Print the type of the JSON-serializable dictionary json_serializable_dict
print(type(json_serializable_dict))

# Print the JSON-serializable dictionary json_serializable_dict
print(json_serializable_dict)

