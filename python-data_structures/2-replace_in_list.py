#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific position."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 9, 5]
    idx = 1
    element = 2
    print("Before: {}".format(my_list))
    replace_in_list(my_list, idx, element)
    print("After: {}".format(my_list))
