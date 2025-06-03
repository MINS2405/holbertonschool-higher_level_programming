#!/usr/bin/python3
'''
This script defines a function to write text into a UTF-8 text file.
'''


def write_file(filename="", text=""):
    '''
    Writes the given text to a UTF-8 text file.
    The function creates the file if it does not exist, or overwrites
    it if it does.
    Returns the number of characters written.
    '''
    with open('filename', mode="w", encoding="UTF-8") as filename:
        filename = filename.write(text)
        print(filename, text)
