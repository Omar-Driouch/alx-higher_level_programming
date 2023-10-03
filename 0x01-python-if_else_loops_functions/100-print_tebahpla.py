#!/usr/bin/python3
for char in range(25, -1, -2):
    print("{:s}{:s}".format(chr(char + ord("a")),
          chr(char - 1 + ord("a")).upper()), end="")
