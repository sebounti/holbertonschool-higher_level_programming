#!/usr/bin/python3
'''
this module

'''


def write_file(filename="", text=""):
    '''
    This function writes the specified text to a file.

    Parameters:
        filename (str): The name of the file to write to.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    '''
    with open(filename, "w", encoding="utf-8") as my_file:
        characters_written = my_file.write(text)

        return characters_written
