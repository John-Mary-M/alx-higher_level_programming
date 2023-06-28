#!/usr/bin/python3
'''This module defines a class Square that defines a square based on the script
5-square.py
'''


class Square:
    '''
    Represents a square object.
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        Initializes instance of a square
        Args:
        __size(int): size of the square
        Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than 0.
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''
        Retrieves the size of the square.
        Returns:
        int: The size of the square.
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        Sets the size of the square.
        Args:
        value (int): The new size of the square.
        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._Square__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        '''sets the position of the square in 2d space
        '''
        if not isinstance(value, tuple) or len(value) != 2 \
           or not all(isinstance(num, int) for num in value) or \
           not all(num >= 0 for num in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value


    def area(self):
        '''
        Calculates and returns area of a square based on size
        Returns:
        int: The area of the square
        '''
        return(self.__size**2)

    def my_print(self):
        '''
        Prints to stdout the square with the character #
        Args:
        self
        Attributes:
        None
        '''
        if self.size == 0:
            print()
        for i in range(self.size):
            print('#' * self.size, end='')
            print()
