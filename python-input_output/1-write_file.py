#!/usr/bin/python3
"""
in the module the write_file function is declared
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
