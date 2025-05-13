# Python - More Data Structures: Set, Dictionary 🐍

Welcome! This project will help you discover two powerful data structures in Python: sets and dictionaries. Here you’ll find simple explanations, code examples, and tips to help you get started. Ready? Let’s go! 🎉


## 🌟 Sets

A set is a collection of unique, unordered elements.


➕ Creating a set

fruits = {"apple", "banana", "orange"}
print(fruits)  # {'orange', 'banana', 'apple'}


🚫 Adding and removing elements

fruits.add("kiwi")
print(fruits)  # {'orange', 'banana', 'apple', 'kiwi'}

fruits.remove("banana")
print(fruits)  # {'orange', 'apple', 'kiwi'}


🔄 Set operations

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)  # Union: {1, 2, 3, 4, 5}
print(set1 & set2)  # Intersection: {3}
print(set1 - set2)  # Difference: {1, 2}


## 📖 Dictionaries

A dictionary stores pairs of keys and values. It's great for quickly looking up information!


➕ Creating a dictionary

person = {"name": "Alice", "age": 25}
print(person["name"])  # Alice


📝 Add, update, and delete

person["city"] = "Paris"   # Add
person["age"] = 26         # Update
del person["name"]         # Delete
print(person)  # {'age': 26, 'city': 'Paris'}


🔄 Loop through a dictionary

for key, value in person.items():
    print(key, ":", value)
age : 26
city : Paris


## 💡 Useful Functions

🔢 Lambda, map, filter

### lambda: a short, anonymous function

square = lambda x: x * x
print(square(4))  # 16

map: applies a function to each element

numbers = [1, 2, 3]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6]

### filter: 

filters elements by a condition

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2]

## 📚 Example Functions

1. Square all elements in a matrix

def square_matrix(matrix):
    return [[x**2 for x in row] for row in matrix]

print(square_matrix([[1, 2], [3, 4]]))  # [[1, 4], [9, 16]]


2. Replace an element in a list

def replace_in_list(lst, old, new):
    return [new if x == old else x for x in lst]

print(replace_in_list([1, 2, 1], 1, 99))  # [99, 2, 99]


3. Sum of unique elements

def uniq_add(my_list):
    return sum(set(my_list))

print(uniq_add([1, 2, 2, 3]))  # 6


4. Common elements in two sets

def common_elements(set_1, set_2):
    return set_1 & set_2

print(common_elements({1, 2, 3}, {2, 3, 4}))  # {2, 3}


5. Elements present in only one set

def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2

print(only_diff_elements({1, 2}, {2, 3}))  # {1, 3}


6. Number of keys in a dictionary

def number_keys(a_dictionary):
    return len(a_dictionary)

print(number_keys({"a": 1, "b": 2}))  # 2


7. Print a sorted dictionary

def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")

print_sorted_dictionary({"b": 2, "a": 1})
a: 1
b: 2


## 🎯 Tips

* Try each example in a .py file to see the result.

* Use the type() function to check your variable types.

* Read the official Python documentation to learn more!


## AUTHOR

MINS2405