#!/usr/bin/python3
"""This module uses 2 imported functions."""
import os
import sys
import json

"""Import 2 previous functions from previous files."""
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

"""Check if the file exists. If not, create a new one"""
filename = 'add_item.json'
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

"""Add the arguments."""
items.extend(sys.argv[1:])

"""Save the updated list as a JSON file"""
save_to_json_file(items, filename)
