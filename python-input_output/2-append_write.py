#!/usr/bin/python3
'''
This script defines a function to append text to a UTF-8 text file.
'''


def append_write(filename="", text=""):
    '''
    Appends the given text to the end of a UTF-8 text file.
    If the file does not exist, it will be created.
    Returns the number of characters added.
    '''
    with open(filename, mode="a", encoding="UTF-8") as f:
        return f.write(text)
