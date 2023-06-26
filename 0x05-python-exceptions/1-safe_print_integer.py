#!/usr/bin/python3


def safe_print_integer(value):
    '''
    Prints an integer with "{:d}".format()
    '''
    try:
        print("{:d}".format(value))
        return True  # Return True if the value is an integer
    except (ValueError, TypeError):  # If a ValueError or TypeError occurs
        return False  # Return False if the value is not an integer
