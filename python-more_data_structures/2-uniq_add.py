#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""
    unique_list = set(my_list)
    sum_unique = sum(unique_list)
    return sum_unique
