#!/usr/bin/python3
"""This module has a class inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a class."""
    def __init__(self, width, height):
        """Initialize with height and width"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height

    def __str__(self):
        """Returns a string"""
        return f"[Rectangle] {self._width}/{self._height}"

    def area(self):
        return self._width * self._height
