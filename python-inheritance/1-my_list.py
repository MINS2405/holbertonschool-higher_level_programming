#!/usr/bin/python3


'''
Defines the MyList class, which extends the built-in list type.
'''


class MyList(list):
    '''
    Custom list class with an additional method for sorted printing.
    '''

    def print_sorted(self):
        '''
        Displays the list elements in ascending order.
        '''
        print(sorted(self))
