#!/usr/bin/python3
"""
Write a function that prints a matrix of integers.

Prototype: def print_matrix_integer(matrix=[[]]):
Format: see example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers
"""
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]


print_matrix_integer(matrix)
print("--")
print_matrix_integer()
