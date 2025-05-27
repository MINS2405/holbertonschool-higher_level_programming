#!/usr/bin/python3


'''
Defines the BaseGeometry class with essential geometry
validation features.
'''


class BaseGeometry:
    '''
    Serves as a blueprint for geometric objects and provides
    validation methods.
    '''

    def area(self):
        '''
        Must be implemented by subclasses; raises an Exception
        if called directly.
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Ensures that value is a positive integer.

        Args:
            name (str): The name of the parameter to check.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        '''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


'''
Implements the Rectangle class, which extends BaseGeometry with
width and height.
'''


class Rectangle(BaseGeometry):
    '''
    Rectangle models a four-sided shape with right angles.
    '''

    def __init__(self, width, height):
        '''
        Constructs a Rectangle after validating width and height.

        Args:
            width (int): The rectangle's width.
            height (int): The rectangle's height.
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''
        Calculates the area of the rectangle.
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        Provides a string representation of the Rectangle instance.
        '''
        return f"[Rectangle] {self.__width}/{self.__height}"


'''
Defines the Square class, a special Rectangle with equal sides.
'''


class Square(Rectangle):
    '''
    Square represents a rectangle with all sides of equal length.
    '''

    def __init__(self, size):
        '''
        Initializes a Square instance, ensuring size is valid.

        Args:
            size (int): The length of each side of the square.
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        '''
        Returns a string that describes the Square object.
        '''
        return f"[Square] {self.__size}/{self.__size}"
