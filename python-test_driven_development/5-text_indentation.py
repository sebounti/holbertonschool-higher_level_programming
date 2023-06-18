#!/usr/bin/python3
"""
Module text_indentation
Adds two new lines after a set of characters.
"""


def text_indentation(text):
    """
    prints a text with 2 new
    lines after each of ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    my_text = ""
    for char in text:
        if char in [".", "?", ":"]:
            my_text += char + "\n\n"
        else:
            my_text += char
    print(my_text)
