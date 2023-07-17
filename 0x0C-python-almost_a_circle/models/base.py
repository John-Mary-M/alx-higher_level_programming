#!/usr/bin/python3
"""Class base"""
import json


class Base:
    """The class template"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json string"""
        return json.dumps(list_dictionaries or [])
