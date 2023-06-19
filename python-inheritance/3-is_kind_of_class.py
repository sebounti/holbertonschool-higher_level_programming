#!/usr/bin/python3
"""
This script defines a function called is_kind_of_class that checks if an object
 is an instance of a specified class or a subclass of that class.
"""


def is_kind_of_class(obj, a_class):
    '''
    Checks if the object is an instance of the specified class
    or a subclass of that class.

    Args:
        obj: The object to check the type of.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of the specified class
          or a subclass of that class, False otherwise.

    '''
    if type(obj) is a_class or issubclass(type(obj), a_class):
        return True

    return False
