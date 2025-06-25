#!/usr/bin/python3
""" This module has a class inheriting from list"""


class MyList(list):
    """This class is a subclass of list."""
    def print_sorted(self):
        print(sorted(self))
