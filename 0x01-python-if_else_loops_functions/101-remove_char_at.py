#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for index, character in enumerate(str):
        if index != n:
            new = new + character
    return(new)
