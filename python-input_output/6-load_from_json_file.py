#!/usr/bin/python3
"""This module creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """
    deserializes object from json file

    Args:
        filename(str): json file
    """
    with open(filename, "r+", encoding="utf-8") as my_file:
        return_obj = json.load(my_file)

    return (return_obj)
