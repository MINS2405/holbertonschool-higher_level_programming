# python-data_structures

# 0️⃣ 0-print_list_integer.py

# Print a List of Integers 🖨️

#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))


# 1️⃣ 1-element_at.py

# Retrieve an Element Safely 🔍

#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]


# 2️⃣ 2-replace_in_list.py

# Replace an Element in a List 🔄

#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list


# 3️⃣ 3-print_reversed_list_integer.py

# Print List in Reverse Order 🔁

#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in reversed(my_list):
        print("{:d}".format(i))


# 4️⃣ 4-new_in_list.py

# Replace in a Copy of the List 📝

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list


# 5️⃣ 5-no_c.py

# Remove All 'c' and 'C' from a String 🚫

#!/usr/bin/python3
def no_c(my_string):
    return "".join([ch for ch in my_string if ch != 'c' and ch != 'C'])


# 6️⃣ 6-print_matrix_integer.py

# Print a Matrix of Integers 🧮

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(i) for i in row))


# 7️⃣ 7-add_tuple.py

# Add Two Tuples ➕

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a1 + b1, a2 + b2)


# 8️⃣ 8-multiple_returns.py

# Return Length and First Character of String 📝

#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])


# 9️⃣ 9-max_integer.py

# Find the Biggest Integer in a List 🏆

#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_num = my_list[0]
    for i in my_list:
        if i > max_num:
            max_num = i
    return max_num


# 🔟 10-divisible_by_2.py

# Find Multiples of 2 in a List ✌️

#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [i % 2 == 0 for i in my_list]


# 1️⃣1️⃣ 11-delete_at.py

# Delete an Item at a Specific Index ❌

#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list


# 1️⃣2️⃣ 12-switch.py

# Switch Values of Two Variables 🔄

#!/usr/bin/python3
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))

# AUTHOR

MINS2405