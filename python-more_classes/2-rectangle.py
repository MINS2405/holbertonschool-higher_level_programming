#!/usr/bin/python3
"""
This module defines the Rectangle class which allows you to create rectangles
with a width and a height, and calculate their area.
The class also validates the values given for width and height.
"""


class Rectangle:
    """
    Rectangle class that represents a rectangle
    defined by its width and height.

    Private attributes:
        __width (int): width of the rectangle (must be >= 0)
        __height (int): height of the rectangle (must be >= 0)

    Properties:
        width: get or set the width, with type and value validation
        height: get or set the height, with type and value validation

    Public methods:
        area(): returns the area of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the rectangle's width, with validation.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the rectangle's height, with validation.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height
