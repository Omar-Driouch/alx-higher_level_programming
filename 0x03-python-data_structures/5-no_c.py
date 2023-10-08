#!/usr/bin/env python3
def no_c(my_string):
    tr = str.maketrans('', '', 'Cc')
    return (my_string.translate(tr))
