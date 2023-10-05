#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    num_arguments = len(arguments)
    if num_arguments == 0:
        print("0 arguments.")
    elif num_arguments == 1:
        print("{} argument:".format(num_arguments))
    else:
        print("{} argument:".format(num_arguments))
    for i, arg in enumerate(arguments, start=1):
        print("{}: {}".format(i, arg))
