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
    if num_arguments >= 1:
        num_arguments = 0
        for arg in sys.argv:
            if num_arguments != 0:
                print("{}: {}".format(num_arguments, arg))
            num_arguments += 1
