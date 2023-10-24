#!/usr/bin/python3
"""Class Square with size"""


class Square:
    """Class to create a square with it size"""

    def __init__(self, size):
        """Constructor of the Square"""
        if isinstance(size, int):
            raise TypeError
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
