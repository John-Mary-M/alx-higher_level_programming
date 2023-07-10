#!/usr/bin/python3
"""this module is definition of inherits_from()"""


def inherits_from(obj, a_class):
    """
    Retruns True if sub class, False if not
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
