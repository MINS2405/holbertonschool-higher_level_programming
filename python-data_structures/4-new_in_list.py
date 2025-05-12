#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position
    without modifying the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 9, 5]
    idx = 1
    element = 2
    print("Before: {}".format(my_list))
    new_list = new_in_list(my_list, idx, element)
    my_list = [1, 2, 3, 4, 5]
    idx = 1
    element = 2
    print("After: {}".format(my_list))
