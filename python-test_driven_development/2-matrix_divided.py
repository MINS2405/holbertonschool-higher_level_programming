#!/usr/bin/python3
"""
Divides all elements of a matrix by a divisor.

This module provides a function to divide all elements of a matrix
(list of lists of integers/floats) by a divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): Matrix of integers/floats.
        div (int or float): The divisor.

    Returns:
        list of lists: New matrix with elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    "" "of integers/floats"
                )

    if len(matrix) > 0:
        row_length = len(matrix[0])
        for row in matrix:
            if len(row) != row_length:
                raise TypeError(
                    "Each row of the matrix must have the same size"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
        [round(element / div, 2) for element in row]
        for row in matrix
    ]

    return new_matrix
