#!/usr/bin/python3
"""writes string to text file and returns number or characters written"""


def write_file(filename="", text=""):
    """writes string to text file and returns number or characters written"""
    with open(filename, mode='w', encoding='utf-8') as file:
        x_ters = file.write(text)
    return (x_ters)
