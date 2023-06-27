#!/usr/bin/python3
"""
This file contains the definition of the Square class.
"""
from models.rectangle import Rectangle


class Square (Rectangle):
    '''
        Constructor of the Square class.
    '''
    def __init__(self, size, x=0, y=0, id=None):
        """
           class constructor

        Args:
            size (int): The size of the square.
            x (int, optional): The x position of the square.
            y (int, optional): The y position of the square.
            id (int, optional): The identifier to assign to the instance.

        """
        super().__init__(size, size, x, y, id)

    moq

    def __str__(self):
        '''Returns a string representation of the Square.'''
        _id = self.id
        x = self.x
        y = self.y
        _size = self.width

        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             _id, x, y, _size)
