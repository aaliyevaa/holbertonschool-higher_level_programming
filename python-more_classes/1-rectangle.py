#!/usr/bin/python3
""" This module has a class Rectangle."""


class Rectangle:
    """ This class defines a rectangle by its width and height."""
    def __init__(self, width=0, height=0):
        """ Initiation with width and height"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """ Get the value of height"""
        return self.__height

    @property
    def width(self):
        """ Get the value of width"""
        return self.__width

    @height.setter
    def height(self, value):
        """ Set the value of heigth with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        """ Set the value of width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
