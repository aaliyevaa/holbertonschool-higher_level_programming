#!/usr/bin/env python3
"""This module serializes and deserializes a custom objects using
pickle module"""
import pickle


class CustomObject:
    """This is a custom class with 3 attributes."""
    def __init__(self, name, age, is_student):
        """Initialization with name, age and is_student
        attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """This method displays the class in the given
        format"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """This method serializes the current instance
        and saves it in a file called <filename> using
        pickle module"""
        try:
            with open(filename, mode='wb') as f:
                pickle.dump(self, f)
        except IOError:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize <filename>."""
        try:
            with open(filename, mode='rb') as f:
                obj = pickle.load(f)
            return obj
        except Exception:
            return None
