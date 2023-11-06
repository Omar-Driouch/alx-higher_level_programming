#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        Initialize Rectangle.

        Parameters:
        - width: width of the rectangle
        - height: height of the rectangle
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
