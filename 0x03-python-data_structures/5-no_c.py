#!/usr/bin/env python3
def no_c(my_string):
    return ''.join(char for char in my_string if char not in ('C', 'c'))

