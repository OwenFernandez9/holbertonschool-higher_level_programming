#!/usr/bin/python3
import json
"""
in the module the save_to_json_file function is declared
"""


def save_to_json_file(my_obj, filename):
    """
    This function writes an object to a text file
    """
    obj_str = json.dumps(my_obj)
    with open(filename, 'w') as file:
        try:
            file.write(obj_str)
        finally:
            file.close()
