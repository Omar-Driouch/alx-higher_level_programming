#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from creating  new  attributes
    but 'first_name' attributes.
    """
    __slots__ = ["first_name"]
