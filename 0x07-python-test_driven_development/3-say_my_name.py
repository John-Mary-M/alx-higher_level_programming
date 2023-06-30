#!/usr/bin/python3
"""This module defines a function say_my_name(first_name, last_name="")"""

def say_my_name(first_name, last_name=""):
    """
    This function prints `My name is <first name> <last name>`

    Args:
    first_name (str): USers first name.
    last_name (str): User's last name. If none is provided default value is a
    space.

    Prints:
    My name is <first name> <last name

    Examples:
    >>> # Doctests are located in tests/3-say_my_name.txt
    >>> # Please refer to 'tests/3-say_my_name.txt' for tests
    """
    # check if first name is a string
    if not isinstance(first_name, (str)):
        raise TypeError('first_name must be a string')

    # check if last_name is a string
    if not isinstance(last_name, (str)):
        raise TypeError('last_name must be a string')

    #check if one name is given
    """
    if first_name == "":
        print(last_name)
    elif last_name == "":
        print("My name is ")
    else:
        raise NameError("You must have at least one name")
    """
    print('My name is {} {}'.format(first_name, last_name))
