#!/usr/bin/python3
weight_average = __import__('100-weight_average').weight_average

my_list = [(9, 5), (6, 2), (3, 3), (2, 7)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))
