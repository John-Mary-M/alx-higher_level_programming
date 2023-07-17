#!/usr/bin/python3
"""This module is a definition of the class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ initiates class """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ gets the size """
        return self.width

    @size.setter
    def size(self, value):
        """ sets the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the square"""
        if args:
            i = 0
            keys = ['id', 'size', 'x', 'y']
            for arg in args:
                setattr(self, keys[i], arg)
                i += 1

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns a dictionary representation of a Square
        """
        square_dict = {'id': self.id, 'size': self.size,
                       'x': self.x, 'y': self.y}
        return square_dict
