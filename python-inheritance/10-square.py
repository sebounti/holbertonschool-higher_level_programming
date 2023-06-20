#!/usr/bin/python3
"""Define a class Square based on 9-rectangle.py"""

Rectangle = __import__("9-rectangle").Rectangle


class Square (Rectangle):

    def __init__(self, size):
        '''Initializes a Square object.'''

        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size
