#!/usr/bin/python3


'''
This module defines the BaseGeometry class.
It provides basic methods for geometric operations and validations.
The area() method must be implemented by subclasses.
The integer_validator() method ensures that a value is a positive integer.
'''


class BaseGeometry:
    """Base class for geometric operations and calculations."""

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Indicates that the method is not implemented
            in the base class.
        """
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
            '''
            The value provided is not an integer, so a TypeError is raised.
            '''
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
            '''
            The value provided is not greater than 0, so a ValueError
            is raised.
            '''
