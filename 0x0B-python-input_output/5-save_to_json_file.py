#!/usr/bin/python3
"""This module is a definition of save_to_json_file(my_obj, filename)"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a JSON
    representation:
    """
    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
