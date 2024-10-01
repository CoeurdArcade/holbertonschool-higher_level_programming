#!/usr/bin/python3
"""Defines a class Student."""

class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name  # Initialize the first name of the student
        self.last_name = last_name   # Initialize the last name of the student
        self.age = age               # Initialize the age of the student

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        # Check if attrs is a list and all elements are strings
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            # Return a dictionary with only the specified attributes
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        # If attrs is not provided or not a valid list, return all attributes
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        # Iterate over the key-value pairs in the provided dictionary
        for k, v in json.items():
            # Set the attribute of the student using the key-value pairs
            setattr(self, k, v)

