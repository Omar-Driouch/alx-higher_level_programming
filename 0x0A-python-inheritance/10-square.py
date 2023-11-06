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
        super().__init__(size, size)

    def area(self):
        """
        Method that returns the area of the square
        """
        return self._Rectangle__width * self._Rectangle__height
