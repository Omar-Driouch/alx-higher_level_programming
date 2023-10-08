#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = [False] * len(my_list)

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            newList[i] = True
    
    return (newList)
