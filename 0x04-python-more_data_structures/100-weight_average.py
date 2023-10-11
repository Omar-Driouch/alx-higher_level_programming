#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    res = 1
    av = 0
    div = 0
    for tuple in my_list:
        for elemnt in tuple:
            res *= elemnt
            div = div + tuple[1]
        av += res
        res = 1
    div /= 2

    return av / div
