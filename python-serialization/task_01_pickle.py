#!/usr/bin/python3
import pickle
class CustomObjet:

def __init__(self, name, age, is_student):
self.name = name
self.age = age
self.is_student = is_student

def display(self):
print("Name:", self.name)
print("Age:", self.age)
print("Is Student:", self.is_student)


mon_objet = {"name": "John", "age": 25, "is_student": True}

with open(''my_file.pkl', 'wb') as file:
pickle.dump(my_objet, file)
with open('my_file.pkl', 'rb') as file:
    objet_charge = pickle.load(file)

print(objet_charge)

def load_object_from_file(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, pickle.UnpicklingError, EOFError, Exception):
        return None
obj = load_object_from_file('my_file.pkl')
print(obj)