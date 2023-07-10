#!/usr/bin/python3
"""This module defines is_same_class """


def is_same_class(obj, a_class):
    """checks if obj is the same class as a_class

    """
    return type(obj) is a_class
