#!/usr/bin/python3
"""This module uses 2 imported functions."""

"""Import sys and json libraries to use their built-in functions."""
import sys
import json
from pathlib import Path

"""Import 2 previous functions from previous files."""
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

"""Check if the file exists. If not, create a new one"""
filename = 'add_itme.json'
if Path(filename).exists():
    items = load_from_json_file(filename)
else:
    items = []

"""Add the arguments."""
items.extend(sys.argv[1:])

"""Save the updated list as a JSON file"""
save_to_json_file(items, filename)
