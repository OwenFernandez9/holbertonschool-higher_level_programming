#!/usr/bin/python3
"""
in te module declarated the function read_file
"""
def read_file(filename=""):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)