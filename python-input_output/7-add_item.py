#!/usr/bin/python3
"""
    This module a script that adds all arguments to a Python list,
    and then save them to a file:
"""
import json
import sys
import os


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def save_strings_from_command_line():
    filename = "./add_item.json"
    obj = []
    length = len(sys.argv)

    if not os.path.exists(filename):
        save_to_json_file(obj, filename)

    obj = load_from_json_file(filename)

    idx = 1
    while idx < length:
        obj.append(sys.argv[idx])
        idx += 1

    save_to_json_file(obj, filename)
