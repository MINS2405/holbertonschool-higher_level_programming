#!/usr/bin/python3
'''
This module defines a function that returns the list of available
attributes and methods of any given object.
'''


def lookup(obj):
    '''
    Returns a list of available attributes and methods of an object.

    Parameters:
        obj: The object to inspect.

    Returns:
        A list containing the names of the object's attributes and methods.
    '''
    return dir(obj)


class Mylis(list):
    '''
    MyList is a subclass of the built-in list.
    It adds a method to print the list sorted in ascending order without
    modifying the original list.
    '''

    def print_sorted(self):
        '''
        Prints the list elements in ascending order.
        Uses the built-in sorted() function to create a sorted copy
        of the list.
        '''
        sorted_list = sorted(self)
        print(sorted(self))
        '''
        The 'pass' statement here has no effect and is not necessary,
        but can be used as a placeholder if additional code is to be added
        later.
        '''


pass
