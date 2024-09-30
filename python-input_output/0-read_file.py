#!/usr/bin/python3
"""
in te module declarated the function read_file
"""


def read_file(filename=""):
    """
    This function open and read file
    """
    with open(filename, 'r') as file:
        content = file.read()
        print(content, end="")
