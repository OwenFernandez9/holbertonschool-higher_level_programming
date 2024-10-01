#!/usr/bin/python3
"""
in the module the load_from_json_file function is declared
"""
import json


def load_from_json_file(filename):
    """
    Create object from a JSON file
    """
    with open(filename, 'r') as file:
        obj = json.load(file)
        return obj
