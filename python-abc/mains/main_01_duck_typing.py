#!/usr/bin/env python3

# Import the necessary classes and functions from the task_01_duck_typing module
from task_01_duck_typing import Circle, Rectangle, shape_info

def main():
    """
    Main function to create shapes and display their information.
    """
    try:
        # Create a Circle object with a radius of 5
        circle = Circle(radius=5)

        # Create a Rectangle object with a width of 4 and a height of 7
        rectangle = Rectangle(width=4, height=7)

        # Display the information (area and perimeter) of the circle
        shape_info(circle)

        # Display the information (area and perimeter) of the rectangle
        shape_info(rectangle)
    except Exception as e:
        # Catch and print any exceptions that occur during the execution
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    # Call the main function to execute the script
    main()

