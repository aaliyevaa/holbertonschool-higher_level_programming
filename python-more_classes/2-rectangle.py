#!/usr/bin/python3
""" This module has a class Rectangle."""


class Rectangle:
    """ This class defines a rectangle based on its width and height"""
    def __init__(self, width=0, height=0):
        """ Initialize with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get width value."""
        return self.__width

    @property
    def height(self):
        """ Get height value."""
        return self.__height

    @width.setter
    def width(self, value):
        """ Set width value with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ Set height value with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ This function returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """This function returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2
