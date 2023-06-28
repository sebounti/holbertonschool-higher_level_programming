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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Change json format in to a file

        Args:
            list_objs (list): instance de Base
        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as my_file:
            my_file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        '''
        Returns the python object of json string representation
        '''
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Creates a new instance of the Rectangle class using the provided
        dictionary.
        '''
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1,)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """

        Returns:
            _type_: _description_
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                data = cls.from_json_string(json_data)
                instances = [cls.create(**instance) for instance in data]
                return instances
        except FileNotFoundError:
            return []
