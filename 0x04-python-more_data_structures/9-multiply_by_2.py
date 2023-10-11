#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result_dictionary = {}

    for key, value in a_dictionary.items():
        result_dictionary[key] = value * 2

    return result_dictionary
