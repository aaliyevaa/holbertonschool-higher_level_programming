#!/usr/bin/python3
""" This module has a function."""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of, or if the object
    is an instance of a class that inherited from the specified one"""
    return isinstance(obj, a_class)
