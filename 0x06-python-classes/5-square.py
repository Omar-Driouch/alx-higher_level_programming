#!/usr/bin/python3
"""This is a definition of a class named Square."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Constructor for the Square class."""
        self.__size = size

    @property
    def size(self):
        """Getter method to get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the area of the square. with # """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print()
            for s in range(self.__size):
                print("#", end = "")
        print()   
