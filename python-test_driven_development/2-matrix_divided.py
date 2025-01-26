#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list): A list of lists of numbers.
        div (int/float): Number to divide matrix elements by.

    Returns:
        list: New matrix with elements divided, rounded to 2 decimals.

    Raises:
        TypeError: Invalid matrix or division number.
        ZeroDivisionError: Division by zero.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(x, (int, float))
                    for row in matrix for x in row)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
