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
        __position (tuple): The position to print the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (length of a side).
            position (tuple): The position (x, y) to print the square.
        Raises:
            TypeError: If size is not an integer or
            position is not a tuple of 2 positive integers.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all(
                    isinstance(num, int) and num >= 0
                    for num in position
                )):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """
        Getter for the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(
                    isinstance(num, int) and num >= 0
                    for num in value
                )):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        The position is used to add spaces and newlines.
        """
        if self.__size == 0:
            print()
            return
        # Print newlines for vertical position
        for _ in range(self.__position[1]):
            print()
        # Print each line of the square with spaces for horizontal position
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
