#!/usr/bin/python3
"""This module has a function."""
import json


def save_to_json_file(my_obj, filename):
    """This function writes <my_obj> to the file <filename>"""
    with open(filename, 'w', encoding='utf-8') as f:
        json_string = json.dumps(my_obj)
        f.write(json_string)
