#!/usr/bin/python3

'''
This function checks if an object is exactly an instance of a specified class.
It returns True if the object is created directly from that class,
and False otherwise (even if the object inherits from the class).
'''
def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class,
    otherwise returns False.
    """
    return type(obj) is a_class
