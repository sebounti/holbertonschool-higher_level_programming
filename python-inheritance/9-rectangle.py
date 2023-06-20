#!/usr/bin/python3
"""This module contains a class Rectangle that
    inherits from BaseGeometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle (BaseGeometry):
    '''This class inherits BaseGeometry'''

    def __init__(self, width, height):
        '''
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        '''
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """ return area of the rectangle"""
        return (self.__height * self.__width)

    def __str__(self):
        """Returns a string representation"""
        width = self.__width
        height = self.__height
        cls = type(self).__name__

        return "[{}] {}/{}".format(cls, width, height)
