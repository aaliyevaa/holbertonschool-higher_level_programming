#!/usr/bin/env python3
"""This module has 2 functions for serialization and
deserialization"""
import json


def serialize_and_save_to_file(data, filename):
    """This function serializes the <data> to JSON string and
    saves it in a file called <filename>"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """This function loads the file <filename> and deserializes
    it"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
