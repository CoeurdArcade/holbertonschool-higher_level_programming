#!/usr/bin/env python3
"""
Serialize and deserialize a Python object using pickle.
"""
import pickle

class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initialize a CustomObject instance.

        :param name: The name of the person.
        :param age: The age of the person.
        :param is_student: Boolean indicating if the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self) -> None:
        """
        Display the details of the CustomObject instance.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str) -> None:
        """
        Serialize the CustomObject instance to a file using pickle.

        :param filename: The name of the file to serialize the object to.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Erreur lors de la sérialisation : {e}")

    @classmethod
    def deserialize(cls, filename: str) -> 'CustomObject':
        """
        Deserialize a CustomObject instance from a file using pickle.

        :param filename: The name of the file to deserialize the object from.
        :return: The deserialized CustomObject instance, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, Exception) as e:
            print(f"Erreur lors de la désérialisation : {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Create a CustomObject instance
    obj = CustomObject("John Doe", 25, True)

    # Display the object details
    obj.display()

    # Serialize the object to a file
    obj.serialize("custom_object.pkl")

    # Deserialize the object from the file
    deserialized_obj = CustomObject.deserialize("custom_object.pkl")

    # Display the deserialized object details if successful
    if deserialized_obj:
        deserialized_obj.display()

