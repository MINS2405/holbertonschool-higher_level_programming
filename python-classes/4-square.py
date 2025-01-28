#!/usr/bin/python3
"""Module defining a Square class."""


class Square:
    """Represents a square with size validation."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): Side length of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current square size.

        Returns:
            int: The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): New size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
