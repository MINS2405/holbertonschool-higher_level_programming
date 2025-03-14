#!/usr/bin/python3
"""Module for Square class"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square

        Args:
            size (int): The size of the square
            position (tuple): The position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value (int): The size to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square

        Args:
            value (tuple): The position to set

        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
