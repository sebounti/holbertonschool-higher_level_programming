#!/usr/bin/python3
''' Define a class Rectangle.'''


class Rectangle:
    ''' Represent a Rectangle '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Initialize a new Rectangle.

        args:
        width (int): The width of the new rectangle.
        height (int): The height of the new rectangle.
        '''
        self. height = height
        self. width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        '''Get/set the height of the rectangle.'''
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        '''Get/set the width of the rectangle.'''
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """ return area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """return perimetre of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        line = str(self.print_symbol) * self.width
        rectangle = line
        for i in range(self.height - 1):
            rectangle += "\n" + line
        return rectangle

    def __repr__(self):
        """"Return a string representation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''
        returns the biggest rectangle based on the area
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
