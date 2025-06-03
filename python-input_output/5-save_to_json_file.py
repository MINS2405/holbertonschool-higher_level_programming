#!/usr/bin/python3
'''
This module provides a function to save a Python object
to a file in JSON format.
'''

import json


def save_to_json_file(my_obj, filename):
    '''
    Writes a Python object to a file using JSON representation.

    Args:
        my_obj: The Python object to serialize.
        filename: The name of the file to write to.

    Returns:
        None
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
