#!/usr/bin/python3
"""Module définissant une classe Square."""


class Square:
    """Représente un carré."""

    def __init__(self, size=0):
        """Initialise un nouveau Square.

        Args:
            size (int): La taille du côté du carré. Par défaut 0.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est négatif.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calcule l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size ** 2
