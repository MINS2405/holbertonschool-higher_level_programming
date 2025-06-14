#!/usr/bin/python3
'''
This line tells the system to use Python 3 to run this script
'''


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
