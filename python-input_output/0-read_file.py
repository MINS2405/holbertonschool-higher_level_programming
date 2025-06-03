#!/usr/bin/python3
'''
This script defines a function to read and print the content of
a UTF-8 text file.
'''


def read_file(filename=""):
    '''
    Reads a UTF-8 text file and prints its content to stdout.
    The filename parameter is the name of the file to read.
    '''

    with open('my_file_0.txt', encoding="UTF-8") as f:
        print(f.read())
