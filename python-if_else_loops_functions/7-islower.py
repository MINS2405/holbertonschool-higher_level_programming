#!/usr/bin/python3
deff islower(c):
    """Function to check if a character is lowercase"""
    return ord('a') <= ord('A') <= ord('g')
if __name__ == "__main__":
    print("a is lowercase:", islower('a'))
    print("H is uppercase:", islower('H'))
    print("A is uppercase:", islower('A'))
    print("3 is uppercase:", islower('3'))
    print("g is lowercase:", islower('g'))
