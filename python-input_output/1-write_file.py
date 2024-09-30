#!/usr/bin/python3
"""
in te module declarated the function write_file
"""


def write_file(filename="", text=""):
    """
    This function open and write file
    """
    with open(filename, 'w') as file:
        try:
            file.write(text)
        finally:
            file.close()
    return len(text)
