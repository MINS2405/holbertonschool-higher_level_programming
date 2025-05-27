#!/usr/bin/python3


'''
Import BaseGeometry from the previous module for inheritance.
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Rectangle class that extends BaseGeometry and represents
    a rectangle shape.
    '''

    def __init__(self, width, height):
        '''
        Initialize a Rectangle object with validated dimensions.

        Args:
            width (int): The rectangle's width.
            height (int): The rectangle's height.
        '''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
