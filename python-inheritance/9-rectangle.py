#!/usr/bin/python3


'''
Implements a Square class that specializes the Rectangle with equal sides.
'''

Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    '''A geometric square, inheriting properties from Rectangle.'''

    def __init__(self, size):
        '''
        Initialize a Square with a validated size.

        Args:
            size (int): The length of each side of the square.
        '''

        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)

    def area(self):
        '''
        Compute and return the area of the square.

        Returns:
            int: The area calculated as size squared.
        '''
        return self.__size ** 2
