#!/usr/bin/python3

# Import the Square class from the '3-square' module
Square = __import__('3-square').Square

def main():
    # Create an instance of Square with side length 3
    my_square_1 = Square(3)

    # Print the area of the square
    print(f"Area: {my_square_1.area()}")

    # Try to access the 'size' attribute and handle AttributeError if it doesn't exist
    try:
        print(my_square_1.size)
    except AttributeError as e:
        print(e)

    # Try to access the '__size' attribute and handle AttributeError if it doesn't exist
    try:
        print(my_square_1.__size)
    except AttributeError as e:
        print(e)

    # Create another instance of Square with side length 5
    my_square_2 = Square(5)

    # Print the area of the second square
    print(f"Area: {my_square_2.area()}")

# Ensure the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()

