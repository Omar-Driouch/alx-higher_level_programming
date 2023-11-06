#!/usr/bin/python3
"Class Rectangle that inherits from BaseGeometry"
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    "Rectangle class"

    def __init__(self, width, height):
        """
        Init method for Rectangle
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Method that returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Method that returns the rectangle description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
