#!/usr/bin/python3
"""this module is based on 6-base_geometry.py and it defines a public instance
method integer_validator(self, name, value)
"""


class BaseGeometry():
    """
    Empty class
    """
    def __init__(self):
        """initialzes empty class"""
        pass

    def area(self):
        """
        Raises Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        name (__str__): name of 'int' to be validated
        Conditions:
        If value  is not an integer: raise a TypeError exception, with the
        message <name> must be an integer.

        if value is less or equal to 0: raise a ValueError exception with the
        message <name> must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
