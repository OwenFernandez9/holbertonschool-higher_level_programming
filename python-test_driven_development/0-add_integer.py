#!/usr/bin/python3
"""
A function that adds 2 integers.
"""

def add_integer(a, b=98):
    try:
        a = int(a)
    except Exception:
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except Exception:
        raise TypeError("b must be an integer")
    return a + b