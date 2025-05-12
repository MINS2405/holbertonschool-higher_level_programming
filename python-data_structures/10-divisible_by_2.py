#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Return a list of True/False depending on whether each
    element is divisible by 2."""
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    for number in my_list:
        if number % 2 == 0:
            print(f"{number} is divisible by 2")
        else:
            print(f"{number} is not divisible by 2")
