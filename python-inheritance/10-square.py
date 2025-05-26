#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        '''
        Initialize a new Square instance with size.
        '''
        self.integer_validator("size", size)
        '''
        Validate that size is a positive integer.
        '''
        super().__init__(size, size)
        '''
        Call parent class constructor with validated size for both width and height.
        '''
        self.__size = size
        '''
        Store size as a private attribute.
        '''

    def area(self):
        '''
        Compute and return the area of the Square.
        '''
        return self.__size ** 2

    def __str__(self):
        '''
        Return the string representation of the Square.
        '''
        return f"[Square] {self.__size}/{self.__size}"
