#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par un nombre.
    Args:
    matrix (list of lists): Matrice d'entiers ou de flottants.
    div (int ou float): Nombre par lequel diviser chaque élémen
    Returns:
    list of lists: Nouvelle matrice avec les éléments divis�
    Raises:
    TypeError: Si matrix n'est pas une liste de listes d'entiers/flottants,
               si les lignes de la matrice n'ont pas la même taille,
               ou si div n'est pas un nombre.
    ZeroDivisionError: Si div est égal à 
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> print(matrix_divided(matrix, 3))
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> print(matrix)
    [[1, 2, 3], [4, 5, 6]]
    """
    if
