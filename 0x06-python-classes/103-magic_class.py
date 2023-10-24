#!/usr/bin/python3
"""Main Class MagicClass"""
import math


class MagicClass:
    """Defines MagicClass"""
    def __init__(self, radius=0):
        """Initializes Data"""
        self.__radius = 0
        if (type(radius) is
                not int or type(radius) is not float):
            raise TypeError('radius must be a number')

    def area(self):
        """Get area"""
        return 2 * math.pi * self.__radius ** 2

    def circumference(self):
        """Get Circumference"""
        return 2 * math.pi * self.__radius
