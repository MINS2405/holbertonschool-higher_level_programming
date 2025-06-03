#!/usr/bin/python3
'''
This module provides a function to write text to a UTF-8 encoded file.
The file will be created if it does not exist, or overwritten if it does.
'''


def write_file(filename="", text=""):
    '''
    Writes the given text to a UTF-8 text file.
    The function creates the file if it does not exist, or overwrites it
    if it does.
    Returns the number of characters written.
    '''
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
