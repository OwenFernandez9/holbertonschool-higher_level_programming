#!/usr/bin/python3
"""
This module contains a function called is inherits from
"""


def inherits_from(obj, a_class):
    """
    a function that returns True if the object is an instance of a class/
      that inherited (directly or indirectly) from /
      the specified class otherwise False.
    """
    return issubclass(obj.__class__, a_class) and type(obj) is not a_class
