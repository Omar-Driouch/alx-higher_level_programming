#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Open the file with the given filename"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
