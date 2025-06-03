#!/usr/bin/python3
'''
This module provides a function to convert a Python object
into its JSON string representation.
'''

import json


def to_json_string(my_obj):
    '''
    Returns the JSON string representation of a Python object.

    Args:
        my_obj: The Python object to convert.

    Returns:
        A string containing the JSON representation of my_obj.
    '''
    return json.dumps(my_obj)
