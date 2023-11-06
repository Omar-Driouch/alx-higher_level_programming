#!/usr/bin/python3
"Class Square that inherits from Rectangle"
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    "Square class"

    def __init__(self, size):
        """
        Init method for Square
        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Method that returns the area of the square
        """
        return self.__size ** 2

    def __str__(self):
        """
        Method that returns string representation of the square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
