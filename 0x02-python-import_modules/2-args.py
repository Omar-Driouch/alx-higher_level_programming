#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numarge = len(sys.argv) - 1

    if numarge == 0:
        print("{} arguments.".format(numarge))
    elif numarge == 1:
        print("{} argument:".format(numarge))
    else:
        print("{} arguments:".format(numarge))

    if numarge >= 1:
        numarge = 0
        for arg in sys.argv:
            if numarge != 0:
                print("{}: {}".format(numarge, arg))
            numarge += 1
