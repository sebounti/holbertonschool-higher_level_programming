#!/usr/bin/python3
"""
this module
"""


def read_file(filename=""):
    """
    read a file

    args:
    filename: file to read

    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end='')
