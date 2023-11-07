#!/usr/bin/python3
""" Definition of the class Student"""


class Student:
	"""Represent a student."""
    

	def __init__(self, first_name, last_name, age):

		"""Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
		self._first_name = first_name
		self._last_name = last_name
		self._age = age
	
	@property
	def	first_name(self):
		"""Getter for first_name."""
		return(self._first_name)
	
	@first_name.setter
	def first_name(self, new_value: str):
		"""Setter for first_name."""
		self._first_name = new_value

	@property
	def	last_name(self):
		"""Getter for last_name."""
		return(self._last_name)
	
	@last_name.setter
	def last_name(self, new_value: str):
		"""Setter for last_name."""
		self._last_name = new_value
	
	@property
	def	age(self):
		"""Getter for age."""
		return(self._age)
	
	@age.setter
	def age(self, new_value: str):
		"""Setter for age."""
		self._age = new_value
	


	def to_json(self):
		"""Return the dictionary representation of a Student instance."""
		return self.__dict__
