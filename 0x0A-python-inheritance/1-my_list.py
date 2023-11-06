#!/usr/bin/python3
"""
This module contains the MyList class.
"""


class MyList(list):
    """
    MyList class that inherits from list.
    """
    def print_sorted(self):
        """
        Method to print a list in sorted ascending order.
        """
        print(sorted(self))
