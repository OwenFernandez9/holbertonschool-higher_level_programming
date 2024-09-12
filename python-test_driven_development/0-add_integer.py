#!/usr/bin/python3
"""
A function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    The code attempts to convert the variables a and b to integers.
    If the conversion fails for a, it raises a TypeError with the message
        "a must be an integer".
    If the conversion fails for b, it raises a TypeError with the message
        "b must be an integer".
    If both conversions are successful, it returns the sum of a and b.
    """
    try:
        a = int(a)
    except Exception:
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except Exception:
        raise TypeError("b must be an integer")
    return a + b
