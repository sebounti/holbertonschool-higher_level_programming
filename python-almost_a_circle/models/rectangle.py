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
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = x

    @property
    def width(self):
        '''
        Getter for the private attribute __width.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter for the private attribute __width.

        Args:
            value (int): The new value for the width.
        '''
        self.__width = value

    @property
    def height(self):
        '''
        Getter for the private attribute __height.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter for the private attribute __height.

        Args:
            value (int): The new value for the height.
        '''
        self.__height = value

    @property
    def x(self):
        '''
        Getter for the private attribute __x.
        '''
        return self.x

    @x.setter
    def x(self, value):
        '''
        Setter for the private attribute __x.

        Args:
            value (int): The new value for the x.
        '''
        self.__x = value

    @property
    def y(self):
        '''
        Getter for the private attribute __y.
        '''
        return self.y

    @y.setter
    def y(self, value):
        '''
        Setter for the private attribute __y.

        Args:
            value (int): The new value for the y.
        '''
        self.__y = value
