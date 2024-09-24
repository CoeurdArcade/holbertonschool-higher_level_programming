#!/usr/bin/python3

# Import the add_attribute function from the 101-add_attribute module
add_attribute = __import__('101-add_attribute').add_attribute

# Define a simple class named MyClass
class MyClass():
    pass

# Create an instance of MyClass
mc = MyClass()

# Add an attribute 'name' with value 'John' to the instance mc
add_attribute(mc, "name", "John")

# Print the newly added attribute 'name' of the instance mc
print(mc.name)

# Attempt to add an attribute 'name' with value 'Bob' to a string object
try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    # If an exception occurs, print the exception type and message
    print("[{}] {}".format(e.__class__.__name__, e))

