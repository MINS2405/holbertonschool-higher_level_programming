#!/usr/bin/python3
def text_indentation(text):
    """
    Imprime un texte avec 2 nouvelles lignes après chaque '.', '?' et ':'.

    Args:
    text (str): Le texte à formater et imprimer.

    Raises:
    TypeError: Si text n'est pas une chaîne de caractères.

    >>> text_indentation("Hello. How are you? I'm fine: thanks.")
    Hello.
    <BLANKLINE>
    How are you?
    <BLANKLINE>
    I'm fine:
    <BLANKLINE>
    thanks.
    <BLANKLINE>
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuation:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line:
        print(current_line.strip(), end="")
