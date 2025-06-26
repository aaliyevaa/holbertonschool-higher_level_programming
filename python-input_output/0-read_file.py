#!/usr/bin/python3
"""This module has a function."""


def read_file(filename=""):
    """This function opens a file and reads it."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
