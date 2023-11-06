#!/usr/bin/python3
"""
This module contains the function inherits_from.
"""


def inherits_from(obj, a_class):
    """
    Function that checks if an object is an instance of a class that
    inherited (directly or indirectly) from the specified class.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
