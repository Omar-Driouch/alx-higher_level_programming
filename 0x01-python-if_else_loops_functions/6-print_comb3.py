#!/usr/bin/python3
for num in range(0, 10):
    for num2 in range(num + 1, 10):
        if num == 8 and num2 == 9:
            print('{}{}'.format(str(num), str(num2)))
        else:
            print('{}{}'.format(str(num), str(num2)), end=', ')
