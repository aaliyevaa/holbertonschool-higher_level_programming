#!/usr/bin/python3
"""This module has a function."""


def append_write(filename='', text=''):
    """This function appends <text> at the end of <filename>"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
