#!/usr/bin/python3
"""
This module defines the Rectangle class.
The Rectangle class allows you to create rectangle objects with
a width and a height, and provides methods to calculate the area
and perimeter.
It also validates that width and height are integers greater
than or equal to zero.
"""


class Rectangle:
    """
    Rectangle class that represents a rectangle defined by its
    width and height.

    Class Attributes:
        number_of_instances (int): Counter for the number of
        Rectangle instances.
        print_symbol: Symbol used for string representation (default: '#').
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return the string representation of the rectangle with print_symbol.

        Returns:
            str: The rectangle represented by lines of print_symbol,
                 or an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        # Utilise print_symbol (qui peut être de n'importe quel type)
        symbol = str(self.print_symbol)
        rectangle = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(rectangle)

    def __repr__(self):
        """
        Return a string that can recreate the same Rectangle
        object using eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print a message when a Rectangle instance is deleted and
        decrement the instance counter.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle with the biggest area, or rect_1 if equal.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size.

        Args:
            size (int): The size of width and height (default is 0).

        Returns:
            Rectangle: A new Rectangle instance (a square).
        """
        return cls(size, size)
