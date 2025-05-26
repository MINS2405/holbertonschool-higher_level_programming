#!/usr/bin/python3
'''
usr: This MyList class inherits from the built-in list class.
It adds a print_sorted method that displays the list elements in
ascending order
without modifying the original list.
'''


class Mylis(list):
    def print_sorted(self):
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
