#!/usr/bin/python3
""" This module has a function returning available attributes of an object"""


def lookup(obj):
    """ Returns a list of available attributes."""
    return list(dir(obj))
