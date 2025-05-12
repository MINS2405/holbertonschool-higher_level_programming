#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C from a string."""
    return my_string.translate({ord('c'): None, ord('C'): None})


if __name__ == "__main__":
    my_string = "Best School"
    print(no_c(my_string))
    my_string = "hicago"
    print(no_c(my_string))
    my_string = "C is fun!"
    print(no_c(my_string))
