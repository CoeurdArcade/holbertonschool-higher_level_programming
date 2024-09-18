#!/usr/bin/python3

# Import the Square class from the '0-square' module
Square = __import__('0-square').Square

def main():
    # Create an instance of the Square class
    square_instance = Square()

    # Print the type of the square_instance
    print(type(square_instance))

    # Print the __dict__ attribute of the square_instance
    print(square_instance.__dict__)

if __name__ == "__main__":
    main()

