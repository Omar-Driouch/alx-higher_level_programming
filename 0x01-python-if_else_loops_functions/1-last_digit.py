#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10  # Ensure a positive last digit

if number < 0:
    last_digit = last_digit * -1

if last_digit < 6 and last_digit != 0:
    print(
        f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
elif last_digit >= 6:
    print(
        f"Last digit of {number} is {last_digit} and is greater than 5")
else:
    print(
        f"Last digit of {number} is {last_digit} and is 0")
