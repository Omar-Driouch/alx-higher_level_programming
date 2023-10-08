#!/usr/bin/python3
def no_c(my_string):
    result = ""
    i = 0
    while i < len(my_string):
        if my_string[i] not in ('c', 'C'):
            result += my_string[i]
        i += 1
    return result

