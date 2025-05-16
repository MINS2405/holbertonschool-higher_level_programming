#!/usr/bin/python3

# This module provides a function to print text with indentation.
# The text_indentation function adds two new lines after '.', '?' or ':'.
# It checks that the input text is a string, otherwise raises a TypeError.
# The function removes leading and trailing spaces from each printed line.
# It processes the input text character by character to handle indentation.


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ['.', '?', ':']
    line = ""
    for char in text:
        line += char
        if char in delimiters:
            print(line.strip())
            print()
            line = ""
    if line:
        print(line.strip())
