#!/usr/bin/python3
""" class MyInt that inherits from int"""


class MyInt(int):
    """MyInt class inherits from int of the python standard library
    """
    def __init__(self, value):
        """initialize class"""
        self.value = value

    def __eq__(self, b):
        """reverse equals to not equals"""
        return self.value != b

    def __ne__(self, b):
        """reverses not equals to equals"""
        return self.value == b
