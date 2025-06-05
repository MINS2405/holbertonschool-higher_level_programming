#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python et le sauvegarde dans un fichier JSON.
    Remplace le fichier s'il existe déjà.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Charge un fichier JSON et désérialise son contenu en dictionnaire Python.
    Retourne le dictionnaire.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
