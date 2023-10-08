#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    sum1 = tuple_a + (0, 0)
    sum2 = tuple_b + (0, 0)
    return sum1[0] + sum2[0], sum1[1] + sum2[1]
