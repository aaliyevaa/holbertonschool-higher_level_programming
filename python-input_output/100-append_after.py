#!/usr/bin/python3
"""This is a module"""


def append_after(filename='', search_string='', new_string=''):
    """Add new lines after a specific line"""
    new_lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            new_lines += [line]
            if search_string in line:
                new_lines += [new_string]
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
