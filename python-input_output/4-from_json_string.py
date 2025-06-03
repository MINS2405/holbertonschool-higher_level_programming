#!/usr/bin/python3
'''
This module provides a function to convert a JSON string
into the corresponding Python data structure.
'''

import json


def from_json_string(my_str):
    '''
    Returns the Python object represented by a JSON string.

    Args:
        my_str: The JSON string to convert.

    Returns:
        The corresponding Python object (dict, list, etc.).
    '''
    return json.loads(my_str)
