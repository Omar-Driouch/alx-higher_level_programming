#!/usr/bin/python3
"""
This module contains the class BaseGeometry.
"""


class BaseGeometry:
    """
    A class called BaseGeometry.
    """

    def area(self):
        """
        Public instance method that raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validates value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
