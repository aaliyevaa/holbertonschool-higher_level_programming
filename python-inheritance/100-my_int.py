#!/usr/bin/python3
"""This module has a class."""


class MyInt(int):
    """A int subclass with reverted == and !="""
    def __eq__(self, other):
        """Reverts equal sign"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Reverts not equal sign"""
        return not super().__ne__(other)
