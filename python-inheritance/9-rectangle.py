#!/usr/bin/python3


'''
Defines the BaseGeometry class with basic geometric validation methods.
'''


class BaseGeometry:
    '''
    BaseGeometry serves as a foundation for geometric shapes.
    '''

    def area(self):
        '''
        Raises an exception to indicate that area() must be implemented
        by subclasses.
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Checks if the value is a positive integer.

        Args:
            name (str): The parameter's name.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        '''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


'''
Implements the Rectangle class, inheriting from BaseGeometry and adding
area calculation.
'''


class Rectangle(BaseGeometry):
    '''
    Rectangle represents a quadrilateral with opposite sides equal.
    '''

    def __init__(self, width, height):
        '''
        Initializes a Rectangle instance after validating dimensions.

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
        Calculates and returns the area of the rectangle.
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        Returns a custom string representation of the Rectangle object.
        '''
        return f"[Rectangle] {self.__width}/{self.__height}"
