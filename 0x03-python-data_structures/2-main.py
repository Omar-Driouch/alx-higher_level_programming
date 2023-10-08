#!/usr/bin/python3
"Write a function that replaces an element of a list at a specific position (like in C)."
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 6, 5]
idx = 3
new_element = 11
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)