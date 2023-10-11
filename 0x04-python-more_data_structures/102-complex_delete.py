#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_delete = set()
    for key, valuee in a_dictionary.items():
        if valuee == value:
            keys_to_delete.add(key)

    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary
