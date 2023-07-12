#!/usr/bin/python3
"""reads a file"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, mode='r', encoding='utf-8') as g:
        for line in g:
            print(line, end="")
