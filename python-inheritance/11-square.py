#!/usr/bin/python3
"""This is a module."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class inherits from Rectangle."""
    def __init__(self, size):
        """Initialize with size"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the size of the square."""
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
