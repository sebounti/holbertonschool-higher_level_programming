#!/usr/bin/python3
'''
This module contains the definition of the Rectangle class.
'''


from models.base import Base


class Rectangle(Base):
    '''
    Define Rectangle

    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Constructor for the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): x of the rectangle's position.
            y (int, optional): y of the rectangle's position.
            id (int, optional): The identifier to assign to the instance.
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = x

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
