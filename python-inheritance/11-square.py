#!/usr/bin/python3
'''11-square.py
'''


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
