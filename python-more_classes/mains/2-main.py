#!/usr/bin/python3

# Import the Rectangle class from the '2-rectangle' module
Rectangle = __import__('2-rectangle').Rectangle

# Define a function to print the area and perimeter of a rectangle
def print_rectangle_details(rectangle):
    # Use f-strings for more readable and efficient string formatting
    print(f"Area: {rectangle.area()} - Perimeter: {rectangle.perimeter()}")

# Create an instance of Rectangle with width 2 and height 4
my_rectangle = Rectangle(2, 4)

# Print the area and perimeter of the initial rectangle
print_rectangle_details(my_rectangle)

# Print a separator line
print("--")

# Update the width and height of the rectangle
my_rectangle.width = 10
my_rectangle.height = 3

# Print the area and perimeter of the updated rectangle
print_rectangle_details(my_rectangle)

