#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        '''
        Initialize a new Rectangle instance with width and height.
        '''
        self.integer_validator("width", width)
        '''
        Validate that width is a positive integer.
        '''
        self.integer_validator("height", height)
        '''
        Validate that height is a positive integer.
        '''
        self.__width = width
        '''
        Store width as a private attribute.
        '''
        self.__height = height
        '''
        Store height as a private attribute.
        '''

    def area(self):
        '''
        Compute and return the area of the Rectangle.
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        Return the string representation of the Rectangle.
        '''
        return f"[Rectangle] {self.__width}/{self.__height}"
