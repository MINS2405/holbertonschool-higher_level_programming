#!/usr/bin/python3

number_of_instances = 0
print_symbol = "#"

def __init__(self, width=0, height=0):
    """Initialize rectangle, increment instance count."""
    self.width = width
    self.height = height
    Rectangle.number_of_instances += 1

@property
def width(self):
    """Get width."""
    return self.__width

@width.setter
def width(self, value):
    """Set width, non-negative integer."""
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value

@property
def height(self):
    """Get height."""
    return self.__height

@height.setter
def height(self, value):
    """Set height, non-negative integer."""
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value

def area(self):
    """Calculate area."""
    return self.__width * self.__height

def perimeter(self):
    """Calculate perimeter."""
    if self.__width == 0 or self.__height == 0:
        return 0
    return 2 * (self.__width + self.__height)

def __str__(self):
    """String representation."""
    if self.__width == 0 or self.__height == 0:
        return ""
    symbol = str(self.print_symbol)
    return "\n".join([symbol * self.__width for _ in range(self.__height)])

def __repr__(self):
    """String for recreation."""
    return f"Rectangle({self.__width}, {self.__height})"

def __del__(self):
    """Print message on deletion, decrement count."""
    print("Bye rectangle...")
    Rectangle.number_of_instances -= 1

@staticmethod
def bigger_or_equal(rect_1, rect_2):
    """Compare two rectangles based on area."""
    if not isinstance(rect_1, Rectangle):
        raise TypeError("rect_1 must be an instance of Rectangle")
    if not isinstance(rect_2, Rectangle):
        raise TypeError("rect_2 must be an instance of Rectangle")
    return rect_1 if rect_1.area() >= rect_2.area() else rect_2
