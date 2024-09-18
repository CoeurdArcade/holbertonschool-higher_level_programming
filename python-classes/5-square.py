#!/usr/bin/python3
"""Defines a Square class."""

class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the Square."""
        return (self.__size * self.__size)

    def perimeter(self):
        """Return the perimeter of the Square."""
        if self.__size == 0:
            return (0)
        return (self.__size * 4)

    def __str__(self):
        """Return the printable representation of the Square.

        Represents the square with the # character.
        """
        if self.__size == 0:
            return ("")

        square = []
        for i in range(self.__size):
            [square.append('#') for j in range(self.__size)]
            if i != self.__size - 1:
                square.append("\n")
        return ("".join(square))

    def __repr__(self):
        """Return the string representation of the Square."""
        return f"Square({self.__size})"

    def __del__(self):
        """Print a message for every deletion of a Square."""
        print("Bye square...")

