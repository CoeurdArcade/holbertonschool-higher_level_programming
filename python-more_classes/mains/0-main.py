#!/usr/bin/python3

# Import the Rectangle class from the '0-rectangle' module using the __import__ function
Rectangle = __import__('0-rectangle').Rectangle

def main():
    # Create an instance of the Rectangle class
    my_rectangle = Rectangle()

    # Print the type of the my_rectangle instance
    print(type(my_rectangle))

    # Print the __dict__ attribute of the my_rectangle instance, which contains the instance's attributes
    print(my_rectangle.__dict__)

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Call the main function to execute the script
    main()

