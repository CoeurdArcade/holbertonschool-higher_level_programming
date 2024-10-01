#!/usr/bin/python3
import os
import sys

# Import necessary modules and classes
Student = __import__('11-student').Student
read_file = __import__('0-read_file').read_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def main():
    # Get the file path from command line arguments
    file_path = sys.argv[1]

    # Check if the file exists and remove it if it does
    if os.path.exists(file_path):
        os.remove(file_path)

    # Create a new Student object
    initial_student = Student("John", "Doe", 23)

    # Convert the student object to a JSON representation
    json_student = initial_student.to_json()

    # Print the initial student details
    print_student_details(initial_student, json_student)

    # Save the JSON representation of the student to a file
    save_to_json_file(json_student, file_path)

    # Read the content of the file to verify it was saved correctly
    read_file(file_path)
    print("\nSaved to disk")

    # Create a new fake student object
    fake_student = Student("Fake", "Fake", 89)
    print_student_details(fake_student)

    # Load the JSON representation of the student from the file
    print("Load dictionary from file:")
    loaded_json_student = load_from_json_file(file_path)

    # Reload the new student object from the JSON representation
    fake_student.reload_from_json(json_student)
    print_student_details(fake_student)

def print_student_details(student, json_representation=None):
    print(student)
    print(type(student))
    if json_representation:
        print(type(json_representation))
    print(f"{student.first_name} {student.last_name} {student.age}")

if __name__ == "__main__":
    main()

