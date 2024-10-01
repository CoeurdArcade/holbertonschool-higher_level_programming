#!/usr/bin/python3

# Import the Student class from the '10-student' module
Student = __import__('10-student').Student

# Create instances of the Student class with specific names and ages
student_john_doe = Student("John", "Doe", 23)
student_bob_dylan = Student("Bob", "Dylan", 27)

# Function to safely convert student to JSON with selected attributes
def safe_to_json(student, attrs):
    try:
        return student.to_json(attrs)
    except AttributeError as e:
        print(f"Error converting to JSON: {e}")
        return {}

# Convert the student instances to JSON representations
json_student_john_doe = safe_to_json(student_john_doe, None)
json_student_bob_dylan_selected = safe_to_json(student_bob_dylan, ['first_name', 'age'])
json_student_bob_dylan_selected_with_middle_name = safe_to_json(student_bob_dylan, ['middle_name', 'age'])

# Print the JSON representations of the students
print("JSON representation of John Doe:", json_student_john_doe)
print("JSON representation of Bob Dylan with selected attributes:", json_student_bob_dylan_selected)
print("JSON representation of Bob Dylan with selected attributes including middle name:", json_student_bob_dylan_selected_with_middle_name)

