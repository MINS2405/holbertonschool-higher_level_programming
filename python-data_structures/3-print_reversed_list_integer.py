#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order."""
    if my_list is not None:
        for i in reversed(my_list):
            print("{:d}".format(i))
    else:
        print("None")


if __name__ == "__main__":
    my_list = [5, 4, 3, 2, 1]
    print_reversed_list_integer(my_list)
