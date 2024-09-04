#!/usr/bin/python3
def print_last_digit(number):
    num_str = str(number)
    num_str = num_str[-1]
    number = int(num_str)
    print("{0}".format(number), end='')
    return number
