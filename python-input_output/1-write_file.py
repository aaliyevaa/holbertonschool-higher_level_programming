#!/usr/bin/python3
"""This module has a function to overwrite a file."""


def write_file(filename='', text=''):
    """This function writes <text> inside the file <filename>"""
    with open(filename, 'w', encoding='utf-8') as f:
        return (f.write(text))
