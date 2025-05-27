#!/usr/bin/python3


'''
This module introduces the Rectangle class, inheriting from BaseGeometry.
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Represents a rectangle using BaseGeometry as a foundation.'''

    def __init__(self, width, height):
        '''
        Create a new Rectangle instance with validated dimensions.

        Args:
            width (int): Rectangle's width.
            height (int): Rectangle's height.
        '''
        # Ensure width is a positive integer
        self.integer_validator("width", width)
        # Ensure height is a positive integer
        self.integer_validator("height", height)
        # Set private attributes for dimensions
        self.__width = width
        self.__height = height
