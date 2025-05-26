#!/usr/bin/python3

class BaseGeometry:
    """Base class for geometric operations and calculations."""
    
    def area(self):
        """Calculate the area of the geometry.
        
        Raises:
            Exception: Indicates that the method is not implemented
            in the base class.
        """
        raise Exception("area() is not implemented")
