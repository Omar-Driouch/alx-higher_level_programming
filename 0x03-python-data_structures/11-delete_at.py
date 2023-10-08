#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    newlist = []
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    for i in range(len(my_list)):
        if i != idx:
            newlist.append(my_list[i])
    return newlist
