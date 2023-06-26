#!/usr/bin/python3
'''
This module contains the definition of the Rectangle class.
'''
from .base import Base


class Rectangle(Base):
    '''
    Constructor for the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): The identifier to assign to the instance.
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = x

        super().__init__(id)

    @property
    def width(self):
        '''
        Getter for the private attribute __width.
        '''
        return self.__width

    @width.setter
    def width(self, width):
        '''
        Setter for the private attribute __width.

        Args:
            value (int): The new value for the width.
        '''
        self.__width = width

    @property
    def height(self):
        '''
        Getter for the private attribute __height.
        '''
        return self.__height

    @height.setter
    def height(self, height):
        '''
        Setter for the private attribute __height.

        Args:
            value (int): The new value for the height.
        '''
        self.__height = height

    @property
    def x(self):
        '''
        Getter for the private attribute __x.
        '''
        return self.x

    @x.setter
    def x(self, x):
        '''
        Setter for the private attribute __x.

        Args:
            value (int): The new value for the x.
        '''
        self.__x = x

    @property
    def y(self):
        '''
        Getter for the private attribute __y.
        '''
        return self.y

    @y.setter
    def y(self, y):
        '''
        Setter for the private attribute __y.

        Args:
            value (int): The new value for the y.
        '''
        self.__y = y
