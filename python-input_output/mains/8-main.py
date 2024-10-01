#!/usr/bin/python3

"""
This script demonstrates the creation of an instance of MyClass,
setting its attributes, and converting it to a JSON representation.
"""

# Import the MyClass from the module '8-my_class'
from my_class import MyClass

# Import the class_to_json function from the module '8-class_to_json'
from class_to_json import class_to_json

def main():
    try:
        # Create an instance of MyClass with the name "John"
        instance = MyClass("John")

        # Set the 'number' attribute of the instance to 89
        instance.number = 89

        # Print the type of the instance
        print(f"Type of instance: {type(instance)}")

        # Print the instance (this will likely call the __str__ or __repr__ method of MyClass)
        print(f"Instance: {instance}")

        # Convert the instance to a JSON representation using the class_to_json function
        json_representation = class_to_json(instance)

        # Print the type of the JSON representation
        print(f"Type of JSON representation: {type(json_representation)}")

        # Print the JSON representation
        print(f"JSON representation: {json_representation}")

    except Exception as e:
        # Print any exceptions that occur
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

