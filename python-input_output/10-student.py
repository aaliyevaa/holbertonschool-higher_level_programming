#!/usr/bin/python3
"""This module has a class Student."""


class Student:
    """This class defines a student by first_name, last_name
    and age"""
    def __init__(self, first_name, last_name, age):
        """Initialize with first_name,last_name, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary"""
        if not attrs:
            return self.__dict__
        return {key: getattr(self, key) for key in attrs is hasattr(self, key)}
