#!/usr/bin/python3

Square = __import__('2-square').Square

def print_square_info(square):
    print(type(square))
    print(square.__dict__)

def main():
    try:
        my_square_1 = Square(3)
        print_square_info(my_square_1)

        my_square_2 = Square()
        print_square_info(my_square_2)

        print(my_square_1.size)
        print(my_square_1.__size)

        my_square_3 = Square("3")
        print_square_info(my_square_3)

        my_square_4 = Square(-89)
        print_square_info(my_square_4)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

