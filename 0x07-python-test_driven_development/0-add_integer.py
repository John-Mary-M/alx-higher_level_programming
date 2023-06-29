#!/usr/bin/python3
"""This module defines a function named add_integer"""

def add_integer(a, b=89):
    """This function takes two integers and returns their sum

    Args:
    a (_int_): first integer
    b (_int_): second integer with default value of 98 if none is parsed to the
    function.
    Usage:

    >>> print(add_integer(1, 2))
    3
    >>> print(add_integer(100, -2))
    98
    >>> print(add_integer(2))
    91
    >>> print(add_integer(100.3, -2))
    98.3
    >>> try:
    ...     print(add_integer(None))
    ... except Exception as e:
    ...     print(e)
    ...
    a must be an integer
    >>>


    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(a) is float:
        int(a)

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    elif type(b) is float:
        int(b)

    return a + b
