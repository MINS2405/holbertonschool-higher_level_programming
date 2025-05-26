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
        Call parent constructor using validated size for both dimensions.
        '''
        self.__size = size
        '''
        Store size as private attribute.
        '''

    def area(self):
        '''
        Calculate and return the square's area.
        '''
        return self.__size ** 2

    def __str__(self):
        '''
        Return formatted string representation.
        '''
        return f"[Square] {self.__size}/{self.__size}"
