#!/usr/bin/python3

# Import the Square class from the '5-square' module
Square = __import__('5-square').Square

def main():
    try:
        # Create a Square instance with size 3
        my_square = Square(3)
        my_square.my_print()

        print("--")

        # Change the size to 10 and print the square
        my_square.size = 10
        my_square.my_print()

        print("--")

        # Change the size to 0 and print the square
        my_square.size = 0
        my_square.my_print()

        print("--")

    except Exception as e:
        # Print any exceptions that occur
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

