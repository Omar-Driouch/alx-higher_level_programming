#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number)
        print(number % 10, end="")
    else:
        print(number % 10, end="")
    return (number % 10)
