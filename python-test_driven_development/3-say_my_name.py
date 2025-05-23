#!/usr/bin/python3

# This function prints "My name is <first name> <last name>"
# It checks that both first_name and last_name are strings.
# If not, it raises a TypeError with an appropriate message.


def say_my_name(first_name, last_name=""):
    """Prints "My name is <first name> <last name>"

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
