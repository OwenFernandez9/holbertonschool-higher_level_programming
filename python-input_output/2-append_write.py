#!/usr/bin/python3
"""
in the module the append_write function is declared
"""


def append_write(filename="", text=""):
    """
    This function opens and writes the file at the end
    """
    with open(filename, 'a') as file:
        try:
            file.write(text)
        finally:
            file.close()
    return len(text)
