#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Function to generate Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
        row.append(1)
        triangle.append(row)
    return triangle
