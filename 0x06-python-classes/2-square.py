#!/usr/bin/python3
'''
This module is a definition of the class Square based on 1-square.py script in
this directory.
'''


class Square:
    '''
    Represents a square.
    '''
    def __init__(self, size=0):
        '''
        initializes instance of a square.

        Args:
        __size(int): size of square (default is 0)
        size must be a positive integer type

        Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
        '''
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
