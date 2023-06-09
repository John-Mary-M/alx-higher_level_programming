#!/usr/bin/python3
"""definition of rectangle class that inherits from BaseGeometry"""


class BaseGeometry:

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value for integer and positive"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return True


"""class rectangle"""


class Rectangle(BaseGeometry):
    """creates rectangle class"""
    def __init__(self, width, height):
        """initializes rectangle"""
        if super().integer_validator("width", width):
            self.__width = width
        if super().integer_validator("height", height):
            self.__height = height
