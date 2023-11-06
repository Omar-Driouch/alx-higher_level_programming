#!/usr/bin/python3
"""Defines an object attribute lookup function."""



def lookup(obj):
    """
    Function that returns the list of attributes and methods of an object.
    Args:
        obj: Any kind of object.
    Returns:
        List of the attributes and methods.
    """
    return dir(obj)
