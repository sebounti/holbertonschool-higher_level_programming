#!/usr/bin/python3
"""Define a class BaseGeometry based on 5-Base_geometry.py"""


class BaseGeometry:
    """An empty class representing the base geometry"""

    def area(self):
        """
        Calculate the area of the geometry
        :return: None
        :raises: Exception - area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate if a value is an integer greater than 0
        :param name: Name of the value
        :param value: Value to be validated
        :return: None
        :raises: TypeError - if value is not an integer
                 ValueError - if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
