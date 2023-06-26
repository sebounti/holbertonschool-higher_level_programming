#!/usr/bin/python3
"""
This file contains the definition of the Base class.
"""


class Base:
    __nb_objects = 0
    '''
    Constructor of the Base class.

        Args:
        id (int, optional): The identifier to assign to the instance.
        If not specified, a new identifier will be generated.
    '''
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
