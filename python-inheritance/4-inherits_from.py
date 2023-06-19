#!/usr/bin/python3
"""
This script defines a function called inherits_from that checks if an
object inherits from a specified class (or is a direct instance of that class).
"""


def inherits_from(obj, a_class):
    if type(obj) == a_class:
        return False
    """
        Checks if the object inherits from a specified class
        (or is a direct instance of that class).

        Args:
        obj: The object to check.
        a_class: The class to check.

        Returns:
        True if the object inherits from the specified class, False otherwise.
    """
    return issubclass(type(obj), a_class)
