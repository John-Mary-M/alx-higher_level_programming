#!/usr/bin/python3
'''
This module defines a class Square based on the script 2-square.py
'''

class Square:
    '''
    Represents a square object.

    '''
    def __init__(self, size=0):
        '''
        Initializes instance of a square
        Args:
        __size(int): size of the square

        Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''
        Calculates and returns area of a square based on size

        Returns:
        int: The area of the square
        '''
        return(self.__size**2)
