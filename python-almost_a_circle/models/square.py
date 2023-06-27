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

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        '''Returns a string representation of the Square.'''
        _id = self.id
        x = self.x
        y = self.y
        _size = self.width

        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             _id, x, y, _size)

    def update(self, *args, **kwargs):
        """Update attributes with variable orderly arguments"""

        if (len(args) > 0):

            num_args = min(len(args), 4)

            self.id = args[0]
            self.size = args[1] if num_args > 1 else self.size
            self.x = args[2] if num_args > 2 else self.x
            self.y = args[3] if num_args > 3 else self.y

        if kwargs is not None:
            for key, val in kwargs.items():
                self.__setattr__(key, val)

    def to_dictionary(self):
        """
         Returns a dictionary representation of the Square object.
        """
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y,
                     }
