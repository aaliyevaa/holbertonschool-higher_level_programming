#!/usr/bin/python3
"""This module has a function."""
def is_same_class(obj, a_class):
    """Checks if an objects is an instance of a specified class"""
    if isinstance(obj, a_class):
        return True
    return False
