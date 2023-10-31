#!/usr/bin/python3
"""
Defines a matrix division function.
that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """ Divide all elements of a matrix.

    Args:
    matrix (list): A list of lists of ints or floats.
    div (int/float): The divisor.
    Raises:
    TypeError: If the matrix contains non-numbers.
    TypeError: If the matrix contains rows of different sizes.
    TypeError: If div is not an int or float.
    ZeroDivisionError: If div is 0.

    Returns:
    A new matrix representing the result of the division.
    """
    if matrix is None:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for element in row:
            if not (isinstance(element, int) or isinstance(element, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats")
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    divided_matrix = []
    for row in matrix:
        divided_row = []
        for element in row:
            result = round(element / div, 2)
            divided_row.append(result)
        divided_matrix.append(divided_row)
    return divided_matrix
