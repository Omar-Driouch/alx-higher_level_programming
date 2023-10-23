#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for index in range(x):
        try:
            i += 1
            print("{}".format(my_list[index]), end="")
        except Exception as inst:
            print(inst)
    print("")
    return (i)
