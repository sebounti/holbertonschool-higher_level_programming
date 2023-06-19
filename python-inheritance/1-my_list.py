#!/usr/bin/python3
"""
Define a class MyList. based on 1-my-list.py
"""


class MyList(list):
    """
Represent mylist.
    """
    def print_sorted(self):
        ''' prints a sorted list in ascending order'''
        print(sorted(self))
