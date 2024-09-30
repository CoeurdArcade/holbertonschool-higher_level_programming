#!/usr/bin/python3

# Import the read_file function from the module '0-read_file'
from read_file import read_file

def main():
    try:
        # Call the read_file function with the argument "my_file_0.txt"
        read_file("my_file_0.txt")
    except FileNotFoundError:
        print("Error: The file 'my_file_0.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

