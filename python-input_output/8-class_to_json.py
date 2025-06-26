#!/usr/bin/python3
"""This module has a function."""


def class_to_json(obj):
    """Returns the dictionary description of an object."""
    return obj.__dict__
