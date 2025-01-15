#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    for arg in sys.argv[1:]:
        try:
            total += int(arg)
        except ValueError:
            print(f"Erreur : '{arg}' n'est pas un nombre valide.")
            sys.exit(1)
    print(total)
