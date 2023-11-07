#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    result[key] = value
            return result

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Args:
            json (dict): A dictionary with key-value pairs
            to replace student attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
