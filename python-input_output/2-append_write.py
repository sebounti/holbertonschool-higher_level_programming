#!/usr/bin/Python3
'''This module defines a function to append text to a file.'''


def append_write(filename="", text=""):
    '''
    This function writes the specified text to a file.

    Parameters:
        filename (str): The name of the file to write to.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    '''
    with open(filename, "a", encoding="utf-8") as my_file:
        characters_added = my_file.write(text)

    return characters_added
