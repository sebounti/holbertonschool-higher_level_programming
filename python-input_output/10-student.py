#!/usr/bin/python3
'''
    This module contains a class Student
'''


class Student:
    '''Initialization of attributes

            Args:
                first_name(str): first attribute
                last_name(str): second attribute
                age(int): third attribute
    '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary
        """
        if attrs is not None and isinstance(attrs, list) and len(attrs) > 0:
            copy_attrs = {}
            for attr in attrs:
                if hasattr(self, attr):
                    copy_attrs[attr] = getattr(self, attr)
            return copy_attrs
        else:
            return (self.__dict__)
