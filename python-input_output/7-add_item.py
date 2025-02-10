#!/usr/bin/python3
'''
7-add_item.py
'''
import sys
import os
import json


def save_to_json_file(my_obj, filename):
    """Saves a Python object to a file in JSON format."""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Loads a Python object from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)


if __name__ == "__main__":
    filename = "add_item.json"

    # Load existing data if the file exists
    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    # Add new arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file(items, filename)
