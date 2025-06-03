#!/usr/bin/python3
'''
This module provides a function to load a Python object
from a JSON file.
'''

import json


def load_from_json_file(filename):
    '''
    Loads a Python object from a JSON file.

    Args:
        filename: The name of the JSON file to read from.

    Returns:
        The Python object represented by the JSON file.
    '''
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
