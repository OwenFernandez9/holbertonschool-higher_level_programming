#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    a = 0
    if not my_list:
        return None
    if x == 0:
        return 0
    
    try:
        for elem in my_list:
            if a >= x:
                break
            print(elem, end="")
            a += 1
        print()
        return a
    except:
        print()
        return None
