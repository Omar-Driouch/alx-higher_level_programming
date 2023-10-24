#!/usr/bin/python3
"""This is a definition of a class named Square."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor for the Square class."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method to get the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
