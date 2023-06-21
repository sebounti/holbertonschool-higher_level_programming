#!/usr/bin/Python3
'''This module  returns the JSON representation of an object (string).'''
import json


def from_json_string(my_str):
    """
      Serializes an object to json

    Args:
        obj(type: any): object to be serialized

    """
    return (json.loads(my_str))
