#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_my_list = list(my_list)
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_my_list[idx] = element
    return new_my_list