#!/usr/bin/python3

# Import the Rectangle class from the module
Rectangle = __import__('7-rectangle').Rectangle

# Create a rectangle with width 8 and height 4
rectangle_1 = Rectangle(8, 4)
print(rectangle_1)
print("--")

# Change the print symbol for rectangle_1
rectangle_1.print_symbol = "&"
print(rectangle_1)
print("--")

# Create a rectangle with width 2 and height 1
rectangle_2 = Rectangle(2, 1)
print(rectangle_2)
print("--")

# Change the print symbol for rectangle_2
rectangle_2.print_symbol = "C"
print(rectangle_2)
print("--")

# Create a rectangle with width 7 and height 3
rectangle_3 = Rectangle(7, 3)
print(rectangle_3)
print("--")

# Change the print symbol for rectangle_3 to a list
rectangle_3.print_symbol = ["C", "is", "fun!"]
print(rectangle_3)
print("--")

