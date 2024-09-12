#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for a in range(x):
            print(my_list[a], end="")
        print()
        return a
    except IndexError:
        print()
        return a
