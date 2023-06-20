#!/usr/bin/python3
"""Define a class Square based on 9-rectangle.py"""

Rectangle = __import__("9-rectangle").Rectangle


class Square (Rectangle):

    def __init__( self, size):
        '''Initializes a Square object.'''
        self.__size = size

        super().__init__(self.__size, self.__size)
        super().integer_validator("size", self.__size)
