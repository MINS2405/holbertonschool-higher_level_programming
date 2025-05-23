#!/usr/bin/python3
# This module defines a function that adds two integers.
# The function performs type checking to ensure inputs are valid.
# It raises a TypeError if either input is not an integer or float.
# If the inputs are floats, they are cast to integers before addition.
# The function returns the sum of the two integers.
"""
This module provides a function to add two numbers.

It checks that the inputs are integers or floats,
casts floats to integers, and raises a TypeError
if the inputs are not valid.
"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
