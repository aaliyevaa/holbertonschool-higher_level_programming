#!/usr/bin/python3
"""This module has a function"""
import json


def from_json_string(my_str):
    """This function deserializes."""
    return json.loads(my_str)
