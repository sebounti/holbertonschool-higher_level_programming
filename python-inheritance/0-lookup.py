#!/usr/bin/python3
"""
This script defines a function called lookup that
returns the list of attributes of an object.
"""


def lookup(obj):
    """
    This function takes an object as input and
    returns the list of its attributes.

    Args:
        obj: The object for which we want to obtain the list of attributes.

    Returns:
        A list containing the names of the object's attributes.
    """
    return dir(obj)
