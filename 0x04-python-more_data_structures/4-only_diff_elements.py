#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return set()
    set_0 = set()

    for elm in set_1:
        if elm not in set_2:
            set_0.add(elm)

    for elm in set_2:
        if elm not in set_1:
            set_0.add(elm)

    return set_0
