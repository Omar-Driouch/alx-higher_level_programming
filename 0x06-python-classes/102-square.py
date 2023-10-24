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
        """Setter method to set the size of the square."""
        if not isinstance(value, int) or not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, other):
        """Less than comparison method."""
        return self.__size < other.__size

    def __le__(self, other):
        """Less than or equal comparison method."""
        return self.__size <= other.__size

    def __eq__(self, other):
        """Equal comparison method."""
        return self.__size == other.__size

    def __ne__(self, other):
        """Not equal comparison method."""
        return self.__size != other.__size

    def __gt__(self, other):
        """Greater than comparison method."""
        return self.__size > other.__size

    def __ge__(self, other):
        """Greater than or equal comparison method."""
        return self.__size >= other.__size
