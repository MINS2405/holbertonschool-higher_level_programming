#!/usr/bin/python3
"""
This module defines the Square class.

The Square class allows you to create square objects with
a private size attribute.
It ensures that the size is always an integer greater than or equal to zero.
If the size is not an integer, a TypeError is raised.
If the size is less than zero, a ValueError is raised.
"""


class Square:
    """
    Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square (must be >= 0).

    Methods:
        __init__(self, size=0):
            Initializes a new Square instance with the given size.
            Raises a TypeError if size is not an integer.
            Raises a ValueError if size is less than zero.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Parameters:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
