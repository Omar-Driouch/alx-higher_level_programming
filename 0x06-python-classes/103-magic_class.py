"""Class MagicClass"""
import math


class MagicClass:
    def __init__(self, radius=0):
        self.__radius = 0
        if (type(radius) is
                not int or type(radius) is not float):
            raise TypeError('radius must be a number')

    def area(self):
        return 2 * math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius
