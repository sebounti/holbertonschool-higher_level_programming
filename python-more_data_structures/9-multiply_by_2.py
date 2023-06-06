#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDictionary = {}
    for key, value in a_dictionary.items():
        newDictionary[key] = value * 2
    return newDictionary
