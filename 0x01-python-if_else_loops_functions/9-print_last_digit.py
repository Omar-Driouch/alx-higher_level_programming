#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number)
        print(number % 10)
    else:
        print(number % 10)
    return (number % 10)
