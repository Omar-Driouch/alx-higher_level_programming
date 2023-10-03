#!/usr/bin/python3
for num in range(100):
    if num < 9:
        print("0{}, ".format(num) ,end="")
    elif num < 99:
        print("{}, ".format(num) ,end="")
    else:
        print("{}".format(num) ,end="")
