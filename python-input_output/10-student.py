#!/usr/bin/python3
'''
10-student.py
'''

"""Defines a Student class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Init new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get dict repr of Student.
        attrs: (Optional) Attributes.
        """
        if isinstance(attrs, list) and all(isinstance(e, str) for e in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
