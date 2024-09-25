#!/usr/bin/python3
"""
this module contains a class called Mylist
"""


class MyList(list):
    """
    a class MyList that inherits from list
    """
    def print_sorted(self):
        number = list(self)
        number = sorted(number)
        print(number)

