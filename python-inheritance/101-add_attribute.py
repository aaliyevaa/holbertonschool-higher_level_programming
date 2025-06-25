#!/usr/bin/python3
"""This module has a function."""


def add_attribute(obj, attr, value):
    """Add new attribute if possible."""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
