#!/usr/bin/python3


'''
This module extends the BaseGeometry class with an integer_validator method.
'''


class BaseGeometry:
    '''Base class for geometric operations and calculations.'''

    def area(self):
        '''Calculate the area of the geometry.

        Raises:
            Exception: Indicates that the method is not implemented
            in the base class.
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validate that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        '''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
