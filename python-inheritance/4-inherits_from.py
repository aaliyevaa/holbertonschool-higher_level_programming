#!/usr/bin/python3
"""This module has a function."""


def inherits_from(obj, a_class):
    """Checks is obj inherits from a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
