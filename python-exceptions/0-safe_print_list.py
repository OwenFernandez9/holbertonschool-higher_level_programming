#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    a = 0
    if not my_list:
        return None
    if x == 0:
        return 0
    try:
        while a < len(my_list) and a < x :
            print(my_list[a], end="")
            a += 1
        print()
        return a
    except:
        print()
        return None
