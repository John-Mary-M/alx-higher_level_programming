#!/usr/bin/python3
"""This module is a definition of a rectangle class"""


class Rectangle():
    """Creates rectangles
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """Calculate the perimeter of the rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        """modifies rectangle to str object
        """
        if not self.perimeter():
            return ""
        return('\n'.join('#' * self.width for x in range(self.height)))
