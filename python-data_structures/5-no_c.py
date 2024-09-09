#!/usr/bin/python3

def no_c(my_string):
    b = ""
    for a in my_string:
        if a != 'c' and a != 'C':
            b += a
    return b
