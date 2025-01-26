#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divise tous les éléments d'une matrice par un nombre."""
    if not all(isinstance(row, list) and
               all(isinstance(x, (int, float)) for x in row)
               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
