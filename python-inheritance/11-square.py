#!/usr/bin/python3
"""Define a class Square based on 9-rectangle.py"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Define the characteristics of the Rectangle class."""

    def __init__(self, size):
        '''Initializes a longeur.

        Args:
            size (int): The size of the square.
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
