#!/usr/bin/python3
""" This module has a class Rectangle."""


class Rectangle:
    """ This class defines a rectangle by its width and height"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize with width and height."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Get the value of width."""
        return self.__width

    @property
    def height(self):
        """ Get the value of height."""
        return self.__height

    @width.setter
    def width(self, value):
        """ Set the value of width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ Set the value of height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("heigth must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return the area of the given rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the given rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ''
        symbol = str(getattr(self, 'print_symbol', Rectangle.print_symbol))
        return "\n".join(
                symbol * self.__width
                for _ in range(self.__height)
                )

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Prints a message upon deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
