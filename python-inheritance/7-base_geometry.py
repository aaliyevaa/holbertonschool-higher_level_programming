#!/usr/bin/python3
"""This module has a class"""


class BaseGeometry:
    """This is a class."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates integers."""
        if type(value) is not int or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
