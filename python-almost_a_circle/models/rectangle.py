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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        '''
        area of the rectangle
        '''
        return self.width * self.height

    def display(self):
        """prints the shape of rectangle with "#" """
        row = self.height
        col = self.width
        x = self.x
        y = self.y

        print("\n" * y, end='')
        for i in range(row):
            print(" " * x, end='')
            for j in range(col):
                print("#", end='')
            print()

    def __str__(self):
        """ return a string """
        _id = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height

        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                _id, x, y, w, h)

    def update(self, *args):

        if args is not None and len(args) > 0:

            num_args = min(len(args), 5)

            self.id = args[0]
            self.width = args[1] if num_args > 1 else self.width
            self.height = args[2] if num_args > 2 else self.height
            self.x = args[3] if num_args > 3 else self.x
            self.y = args[4] if num_args > 4 else self.y
