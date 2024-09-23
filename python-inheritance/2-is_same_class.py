#!/usr/bin/python3
"""
This module contains a function called is same class
"""


def is_same_class(obj, a_class):
    """
    a function that returns True if the object is exactly/
      an instance of the specified class otherwise False.
    """
    return type(obj) is a_class
