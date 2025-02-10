#!/usr/bin/python3
'''
1-write_file.py
 '''


def write_file(filename="", text=""):
    """Write string to file (UTF8), return char count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
