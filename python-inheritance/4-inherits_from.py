#!/usr/bin/python3

'''
This function checks if an object is an instance of a class that inherited
(directly or indirectly) from the specified class.
It returns True if the object's class is a subclass of a_class
(but not a_class itself),
otherwise returns False.
'''

def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a subclass of a_class,
    otherwise returns False.
    """
    # Check that obj is not an instance of a_class itself,
    # but is an instance of a subclass of a_class
    return isinstance(obj, a_class) and type(obj) is not a_class
