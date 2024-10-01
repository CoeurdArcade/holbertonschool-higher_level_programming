#!/usr/bin/python3
"""
Module containing the MyClass class.
"""

class MyClass:
    """
    A simple class to demonstrate basic object-oriented programming concepts.

    Attributes:
        name (str): The name of the instance.
        number (int): A number associated with the instance, default is 0.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of MyClass.

        Parameters:
            name (str): The name to be assigned to the instance.
        """
        self.name = name  # Assign the provided name to the instance
        self.number = 0   # Initialize the number attribute to 0

    def __str__(self) -> str:
        """
        Returns a string representation of the instance.

        Returns:
            str: A string that includes the name and number attributes.
        """
        return f"[MyClass] {self.name} - {self.number:d}"  # Format the string with the instance's name and number

# Example usage:
# if __name__ == "__main__":
#     obj = MyClass("Example")
#     print(obj)

