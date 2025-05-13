#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[i ** 2 for i in row] for row in matrix]
    """Computes the square value of all integers of a matrix."""
    if not matrix:
        return []

    new_matrix = [[x**2 for x in row] for row in matrix]
    return new_matrix
