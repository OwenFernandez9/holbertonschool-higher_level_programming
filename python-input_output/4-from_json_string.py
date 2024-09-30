#!/usr/bin/python3
"""
in the module the from_json_string function is declared
"""
import json


def from_json_string(my_str):
    """
    This function converts the string into a object
    """
    json_obj = json.loads(my_str)
    return json_obj
