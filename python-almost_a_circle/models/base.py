#!/usr/bin/python3
"""
This file contains the definition of the Base class.
"""
import json


class Base:
    '''
    Constructor of the Base class.

        Args:
        id (int, optional): The identifier to assign to the instance.
        If not specified, a new identifier will be generated.
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        """
            class constructor

            Args:
                id(int): public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.
        """
        if (list_dictionaries is None or len(list_dictionaries)) == 0:
            return ("[]")
        else:
            json_string = json.dumps([obj for obj in list_dictionaries])
            return (json_string)
