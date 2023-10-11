#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set(my_list)
    return sum(filter(lambda x: x in unique_numbers, unique_numbers))
