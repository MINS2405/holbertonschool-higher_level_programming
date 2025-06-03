#!/usr/bin/python3
'''
This line tells the system to use Python 3 to run this script
'''


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all(type(attr) is str for attr in attrs):
            ''' Check if attrs is a list of strings
            '''
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        ''' Return only the specified attributes
        '''
        return self.__dict__
    ''' Return all attributes if attrs is not a list of strings
    '''
    def reload_from_json(self, json):
        for key, value in json.items():
            ''' Loop through each key and value in the json dictionary
            '''
            setattr(self, key, value)
            '''
            Set the attribute named key to the value
            '''
