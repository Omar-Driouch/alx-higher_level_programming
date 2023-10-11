#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    av = 0
    div = 0
    for tuple in my_list:
        av = av + tuple[0] * tuple[1]
        div = div + tuple[1]

    return av / div
