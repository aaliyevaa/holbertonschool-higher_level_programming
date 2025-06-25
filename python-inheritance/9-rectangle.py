#!/usr/bin/python3
"""This module has a class inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a class."""
    def __init__(self, width, height):
        """Initialize with height and width"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        return self.__width * self.__height
