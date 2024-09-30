#!/usr/bin/python3
"""
in the module the read_file function is declared
"""


def read_file(filename=""):
    """
    This function open and read file
    """
    with open(filename, 'r') as file:
        content = file.read()
        print(content, end="")
