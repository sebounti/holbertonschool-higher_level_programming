#!/usr/bin/python3
'''
    This module contains a class Student
'''

class Student:
    '''A class representing a student.'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return a dictionary
        """

        return (getattr(self, "__dict__"))
