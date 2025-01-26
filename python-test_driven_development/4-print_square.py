#!/usr/bin/python3
def print_square(size):
    """
    Imprime un carré avec le caractère #.

    Args:
    size (int): La longueur du côté du carré.

    Raises:
    TypeError: Si size n'est pas un entier.
    ValueError: Si size est inférieur à 0.

    >>> print_square(4)
    ####
    ####
    ####
    ####
    >>> print_square(10)
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    >>> print_square(0)
    >>> print_square(1)
    #
    >>> print_square(-1)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
