#!/usr/bin/python3
"""
in the module the to_json_string function is declared
"""
import json


def to_json_string(my_obj):
    """
    This function converts the object into a string
    """
    obj_str = json.dumps(my_obj)
    return obj_str
