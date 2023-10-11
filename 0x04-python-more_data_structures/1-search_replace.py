#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    if 1 <= search <= len(my_list):
        new_list[search - 1] = replace
    return new_list
