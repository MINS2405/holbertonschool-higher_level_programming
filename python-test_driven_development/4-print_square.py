#!/usr/bin/python3
# This module provides a function that prints a square using the '#' symbol.
# The print_square function checks if the input size is a valid integer.
# If the size is not an integer, a TypeError is raised with a clear message.
# If the size is less than 0, a ValueError is raised with
# an appropriate message.
# The function prints a square with sides of length
# 'size' using '#' characters.


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
