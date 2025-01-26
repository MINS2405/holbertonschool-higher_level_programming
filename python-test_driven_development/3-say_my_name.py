#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Imprime "My name is <first name> <last name>"

    Args:
    first_name (str): Le prénom
    last_name (str, optional): Le nom de famille. Par défaut "".

    Raises:
    TypeError: Si first_name ou last_name n'est pas une chaîne de caractères.

    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Bob")
    My name is Bob 
    >>> say_my_name(12, "White")
    Traceback (most recent call last):
        ...
    TypeError: first_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
