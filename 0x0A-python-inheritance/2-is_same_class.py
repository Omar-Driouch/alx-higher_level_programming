#!/usr/bin/python3
"""
This module contains the function is_same_class.
"""


def is_same_class(obj, a_class):
    """
    Function that checks if an object is exactly an instance of a class.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
