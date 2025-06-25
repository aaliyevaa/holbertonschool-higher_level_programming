#!/usr/bin/python3
""" This module has a function returning available attributes of an object"""
def lookup(obj):
    return list(dir(obj))
