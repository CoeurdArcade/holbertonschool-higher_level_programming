#!/usr/bin/python3

# Import the Rectangle class from the module
Rectangle = __import__('8-rectangle').Rectangle

# Create instances of Rectangle
rectangle_1 = Rectangle(8, 4)
rectangle_2 = Rectangle(2, 3)

def compare_rectangles(rect1, rect2):
    """Compare two rectangles and print which one is bigger or equal."""
    if rect1 == Rectangle.bigger_or_equal(rect1, rect2):
        print("rectangle_1 is bigger or equal to rectangle_2")
    else:
        print("rectangle_2 is bigger than rectangle_1")

# Initial comparison
compare_rectangles(rectangle_1, rectangle_2)

# Modify the dimensions of rectangle_2
rectangle_2.width = 10
rectangle_2.height = 5

# Compare again after modification
compare_rectangles(rectangle_1, rectangle_2)

