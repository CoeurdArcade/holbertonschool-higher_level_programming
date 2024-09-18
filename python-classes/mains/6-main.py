#!/usr/bin/python3

def main():
    try:
        Square = __import__('6-square').Square

        # Create a square with size 3 and default position (0, 0)
        my_square_1 = Square(3)
        my_square_1.my_print()

        print("--")

        # Create a square with size 3 and position (1, 1)
        my_square_2 = Square(3, (1, 1))
        my_square_2.my_print()

        print("--")

        # Create a square with size 3 and position (3, 0)
        my_square_3 = Square(3, (3, 0))
        my_square_3.my_print()

        print("--")

    except ImportError as e:
        print(f"Error importing module: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

