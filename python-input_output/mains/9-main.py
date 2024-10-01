#!/usr/bin/python3

# Import the Student class from the '9-student' module
Student = __import__('9-student').Student

# Function to print student details
def print_student_details(student):
    try:
        # Convert the student object to a JSON representation
        student_json = student.to_json()

        # Print the type of the JSON representation
        print(f"Type of JSON representation: {type(student_json)}")

        # Print the 'first_name' field from the JSON representation
        print(f"First Name: {student_json['first_name']}")

        # Print the type of the 'first_name' field
        print(f"Type of First Name: {type(student_json['first_name'])}")

        # Print the 'age' field from the JSON representation
        print(f"Age: {student_json['age']}")

        # Print the type of the 'age' field
        print(f"Type of Age: {type(student_json['age'])}")

    except KeyError as e:
        print(f"Key error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Create a list of Student objects
students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

# Iterate over each student in the list and print their details
for student in students:
    print_student_details(student)

