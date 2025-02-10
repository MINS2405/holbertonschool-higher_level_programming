#!/usr/bin/python3
'''
12-pascal_triangle.py
'''
"""Defines a function to generate Pascal's Triangle."""


def pascal_triangle(n):
    """Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row of Pascal's Triangle

    for i in range(1, n):
        prev_row = triangle[-1]  # Previous row
        new_row = [1]  # Start each row with 1

        # Compute values for the middle of the row
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # End each row with 1
        triangle.append(new_row)  # Add the new row to the triangle

    return triangle
