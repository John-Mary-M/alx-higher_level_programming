#!/usr/bin/python3
"""adds new attribute if possible"""


def add_attribute(obj, attr, value):
    """adds new attribute

    Args:
    obj (__obj__): object to which to add attributes
    attr (__str/int/bool__): attribute to add
    value (__str__): value of attribute.
    """
    if('__slots__' in dir(obj) or '__dict__' not in dir(obj) or
       hasattr(obj, attr)):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
