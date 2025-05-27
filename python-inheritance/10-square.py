#!/usr/bin/python3


'''
Imports the Rectangle class from the previous module for inheritance.
'''
Rectangle = __import__('9-rectangle').Rectangle

'''
Defines the Square class, which is a special case of a Rectangle.
'''


class Square(Rectangle):
    '''
    Square represents a geometric figure with four equal sides.
    '''

    def __init__(self, size):
        '''
        Initializes a Square instance after validating the size.

        Args:
            size (int): The length of each side of the square.
        '''
        if self.integer_validator('size', size):
            self.__size = size
        super().__init__(size, size)

    def area(self):
        '''
        Computes and returns the area specific to the Square.
        '''
        return super().area()
