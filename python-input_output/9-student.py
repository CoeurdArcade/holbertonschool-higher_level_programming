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
        # Initialize the first name of the student
        self.first_name = first_name
        # Initialize the last name of the student
        self.last_name = last_name
        # Initialize the age of the student
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        # Return the dictionary representation of the Student instance
        return self.__dict__

