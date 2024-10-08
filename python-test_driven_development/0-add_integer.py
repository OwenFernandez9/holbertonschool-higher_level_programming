#!/usr/bin/python3
"""
A function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    The code checks if variables a and b are either integers or floats.
    If either variable is not of these types, it raises a TypeError.
    If both variables are valid, it returns their sum.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
