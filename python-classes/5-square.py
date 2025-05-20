#!/usr/bin/python3
"""
square module

This module defines the Square class to create squares,
compute their area, and print them using the '#' character.

Example usage:
    s = Square(3)
    s.my_print()
"""

class Square:
    """
    Class that represents a square.

    Attributes:
        __size (int): The size of the square (length of a side).
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (length of a side).
            Must be an integer >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        Getter for the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with the character '#'.
        If the size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print('#' * self.__size)
