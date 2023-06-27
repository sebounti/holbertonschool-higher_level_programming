#!/usr/bin/python3
"""

"""
from models.rectangle import Rectangle


class Square (Rectangle):
    '''

    '''
    def __init__(self, size, x=0, y=0, id=None):
        """
           class constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return super().__str__()
