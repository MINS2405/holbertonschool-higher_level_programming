#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the maximum integer in a list of integers."""
    if len(my_list) == 0:
        return None

    max_int = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > max_int:
            max_int = my_list[i]

    return max_int


if __name__ == "__main__":
    my_list = [90]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))  # Output: Max: 90
