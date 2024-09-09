#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    max = my_list[0]
    for a in my_list[1:]:
        if a > max:
            max = a
    return max
