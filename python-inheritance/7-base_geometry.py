#!/usr/bin/python3
"""Define a class BaseGeometry based on 5-Base_geometry.py"""


class BaseGeometry:
    """The empty class"""

    def area(self):
        """ return area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
