#!/usr/bin/python3

# Import the Rectangle class from the '6-rectangle' module
Rectangle = __import__('6-rectangle').Rectangle

def main():
    # Create an instance of Rectangle with width 2 and height 4
    my_rectangle_1 = Rectangle(2, 4)

    # Create another instance of Rectangle with width 2 and height 4
    my_rectangle_2 = Rectangle(2, 4)

    # Print the number of Rectangle instances created so far
    print(f"{Rectangle.number_of_instances} instances of Rectangle")

    # Delete the first Rectangle instance
    del my_rectangle_1

    # Print the number of Rectangle instances after deleting the first instance
    print(f"{Rectangle.number_of_instances} instances of Rectangle")

    # Delete the second Rectangle instance
    del my_rectangle_2

    # Print the number of Rectangle instances after deleting the second instance
    print(f"{Rectangle.number_of_instances} instances of Rectangle")

if __name__ == "__main__":
    main()

