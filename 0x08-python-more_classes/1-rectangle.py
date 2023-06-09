#!/usr/bin/python3
"""This module is a definition of a Rectangle class"""


class Rectangle:
    """Makes rectangles"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
