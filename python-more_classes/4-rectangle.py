#!/usr/bin/python3
"""
This module defines the Rectangle class.

The Rectangle class allows you to create rectangle objects with
a width and a height,
and provides methods to calculate the area and perimeter.
It also validates that width and height are integers greater
than or equal to zero.
"""


class Rectangle:
    """
    Rectangle class that represents a rectangle defined by its width
    and height.

    Private attributes:
        __width (int): The width of the rectangle (must be >= 0)
        __height (int): The height of the rectangle (must be >= 0)

    Properties:
        width: Get or set the width, with type and value validation.
        height: Get or set the height, with type and value validation.

    Public methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
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
        """
        Get the width of the rectangle.

        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle, with validation.

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
        """
        Get the height of the rectangle.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle, with validation.

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
        Calculate and return the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter (2 * (width + height)),
            or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Return the string representation of the rectangle with '#' characters.

        Returns:
            str: The rectangle represented by lines of '#' characters,
                 or an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for _ in range(self.__height):
            result += "#" * self.__width + "\n"
        return result.rstrip()
    """ This is just a string, not a Rectangle object """
    mon_rectangle = "Rectangle(2, 4)"


""" This is not valid Python syntax and will cause an error """
"Rectangle(2, 4)" = repr("my_rectangle")

""" This will create a new Rectangle object if the class Rectangle exists """
nouveau_rectangle = eval("Rectangle(2, 4)")
