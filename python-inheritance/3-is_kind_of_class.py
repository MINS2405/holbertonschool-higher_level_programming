#!/usr/bin/python3

'''
This function checks if an object is an instance of a specified class
or an instance of a class that inherited from the specified class.
It returns True if the object is related to the class by inheritance,
otherwise it returns False.
'''

def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or a class
    that inherited from a_class,
    otherwise returns False.
    """
    return isinstance(obj, a_class)
