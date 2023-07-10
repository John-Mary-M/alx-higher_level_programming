#!/usr/bin/python3
"""This module is a definition of Mylist class."""

class MyList(list):
    """MyList class inherits from list class of the python standard
    library.
    """
    def print_sorted(self):
        """
        prints lists sorted in ascending order

        Args:
        self (__int__): list to be sorted
        """
        print(sorted(self))
