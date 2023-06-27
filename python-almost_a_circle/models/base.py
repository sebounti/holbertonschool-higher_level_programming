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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
           Converts a list of dictionaries to a JSON string.

             Args:
                list_dictionaries (list): List of dictionaries to be converted.

            Returns:
                str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries is []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)
