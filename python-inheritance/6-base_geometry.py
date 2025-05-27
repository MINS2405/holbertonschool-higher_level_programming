#!/usr/bin/python3


'''
This module defines the BaseGeometry class.
It provides a base for geometric operations and calculations.
The area() method is not implemented and must be overridden by subclasses.
'''


class BaseGeometry:
    """Base class for geometric operations and calculations."""
    
    def area(self):
        """Calculate the area of the geometry.
        
        Raises:
            Exception: Indicates that the method is not implemented
            in the base class.
        """
        raise Exception("area() is not implemented")
