#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    order_dictionary = sorted(a_dictionary)
    for a in order_dictionary:
        print(f"{a}: {a_dictionary[a]}")