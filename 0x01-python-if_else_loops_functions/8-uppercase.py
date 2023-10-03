#!/usr/bin/python3
def uppercase(str):
    for cha in str:
        if 'a' <= cha <= 'z':
            min = ord('a') - ord('A')
        else:
            min = 0
        print("{:s}".format(chr(ord(cha) - min)), end="")
    print("")
