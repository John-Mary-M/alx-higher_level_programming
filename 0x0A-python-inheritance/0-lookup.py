#!/usr/bin/python3
"""This module is a definition of lookup function"""


def lookup(obj):
    """lookup(obj) returns list of available attributes andd methods of an obj

    Args:
    obj (__obj__): object to be looked up

    """
    return [x for x in dir(obj)]
