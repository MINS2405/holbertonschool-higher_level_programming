#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list."""
    multiples_of_2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples_of_2.append(True)
        else:
            multiples_of_2.append(False)
    return multiples_of_2


if __name__ == "__main__":

 my_list = [0, 1, 2, 3, 4, 5, 6]
for number in my_list:
    if number % 2 == 0:
        print(f"{number} is divisible by 2")
    else:
        print(f"{number} is not divisible by 2")
