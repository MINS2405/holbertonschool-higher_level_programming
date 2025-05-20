#!/usr/bin/python3
"""
This module defines the Square class with a private size attribute.
It allows the creation of square objects with encapsulated size.
"""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initializes a new Square instance with a given size."""
        self.__size = size
