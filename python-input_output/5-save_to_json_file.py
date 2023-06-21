#!/usr/bin/python3
'''this module writes an Object to a text file, using a JSON representation'''
import json


def save_to_json_file(my_obj, filename):
    """
    Serializes object to json file

    Args:
        my_obj: object to be serialized
        filename(str): filename of file accepting json
    """
    with open(filename, "w+", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
