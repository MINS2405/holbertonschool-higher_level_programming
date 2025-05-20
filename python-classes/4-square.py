#!/usr/bin/python3
"""
This module defines the Square class.
The Square class allows you to create square objects with
a private size attribute.
It ensures that the size is always an integer greater than or equal
to zero.
If the size is not an integer, a TypeError is raised.
If the size is less than zero, a ValueError is raised.
The class also provides a property to get and set the size,
and a method to calculate the area.
"""


class Square:
    """
    Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square (must be >= 0).

    Methods:
        area():
            Returns the area of the square.
        size (property):
            Gets or sets the size of the square with validation.
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

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Parameters:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
