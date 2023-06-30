#!/usr/bin/python3
"""This module defines a fuction that prints a square using #"""

def print_square(size):
    """
    print_square prints a square using '#' character

    Args:
    size (int): length of the square

    Usuage:
    print_square(4)

    For examples and doctest test cases refer to ./tests/4-print_square.txt
    """
    # check if size is an integer
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")

    # check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # check if size is a float & less than 0
    if isinstance(size, (float)) and size < 0:
        raise TypeError("size must be an integer")

    for length in range(size):
        for width in range(size):
            print('#', end="")
        print()
