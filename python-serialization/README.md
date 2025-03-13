# holbertonschool-higher_level_programming - python-serialization

**Project Badge:** 100%

**By: Javier Valenzani**

## Description

This project explores marshaling and serialization, fundamental concepts for efficient data storage and transmission. The goal is to enhance your understanding and practical skills in handling data in real-world applications. You'll delve into how data can be transformed and communicated between different parts of a system, or even across different systems, using various formats.

## Introduction

Marshaling and serialization are essential for efficient data handling in computer science. This project delves into how data can be transformed and communicated between systems, focusing on practical implementation and understanding.

**What is Marshaling?**

Marshaling is the process of transforming memory objects into a format suitable for storage or transmission over a network.

**What is Serialization?**

Serialization converts data structures or object states into a format that can be easily saved to a file or sent over a network, preserving the object's state for later recreation.

## Learning Objectives

*   Understand the differences and similarities between marshaling and serialization.
*   Implement serialization in practical tasks.
*   Understand how serialized data is used in web applications, databases, and network communications.
*   Evaluate the performance implications of different serialization formats.

## Resources

*   [Real Python Serialization](https://realpython.com/python-serialization/)
*   [Real Python: Working With JSON Data in Python](https://realpython.com/python-json/)
*   [Python’s pickle documentation](https://docs.python.org/3/library/pickle.html)
*   [Corey Schafer on Pickle](https://www.youtube.com/watch?v=2Tw3wq5eQ-k)
*   [CSV to JSON in Python](https://www.geeksforgeeks.org/convert-csv-to-json-using-python/)
*   [Python XML ElementTree Guide](https://docs.python.org/3/library/xml.etree.elementtree.html)
*   [Socket Programming Guide](https://realpython.com/python-sockets/)

## Tasks

### 0. Basic Serialization

Create a module to serialize a Python dictionary to a JSON file and deserialize the JSON file back to a dictionary.

#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
"""Serializes a Python dictionary to a JSON file."""
with open(filename, 'w') as f:
json.dump(data, f)

def load_and_deserialize(filename):
"""Loads and deserializes data from a JSON file to a Python dictionary."""
try:
with open(filename, 'r') as f:
data = json.load(f)
return data
except FileNotFoundError:
return None

Example usage
data_to_serialize = {"name": "John Doe", "age": 30, "city": "New York"}
serialize_and_save_to_file(data_to_serialize, 'data.json')
print("Data serialized and saved to 'data.json'.")
deserialized_data = load_and_deserialize('data.json')
print("Deserialized Data:")
print(deserialized_data)


### 1. Pickling Custom Classes

Serialize and deserialize custom Python objects using the `pickle` module.

#!/usr/bin/env python3
import pickle

class CustomObject:
"""A custom Python object for demonstration of pickling."""
def init(self, name, age, is_student):
self.name = name
self.age = age
self.is_student = is_student

def display(self):
    """Prints out the object’s attributes."""
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Is Student: {self.is_student}")

def serialize(self, filename):
    """Serializes the current instance to a file using pickle."""
    try:
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
    except Exception as e:
        print(f"Error during serialization: {e}")

@classmethod
def deserialize(cls, filename):
    """Deserializes an instance from a file using pickle."""
    try:
        with open(filename, 'rb') as f:
            obj = pickle.load(f)
        return obj
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error during deserialization: {e}")

Example
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()
obj.serialize("object.pkl")
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
new_obj.display()


### 2. Converting CSV Data to JSON Format

Convert CSV data to JSON format using serialization techniques.

#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename, json_filename="data.json"):
"""Converts CSV data to JSON format."""
try:
with open(csv_filename, 'r') as csvfile:
csv_reader = csv.DictReader(csvfile)
data = list(csv_reader)

    with open(json_filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

    return True
except FileNotFoundError:
    print(f"Error: File '{csv_filename}' not found.")
    return False
except Exception as e:
    print(f"An error occurred: {e}")
    return False

Example usage
csv_file = "data.csv"
if convert_csv_to_json(csv_file):
print(f"Data from {csv_file} has been converted to data.json")


Create a sample `data.csv` file:

name,age,city
John,28,New York
Alice,24,Los Angeles
Bob,22,Chicago
Eve,30,San Francisco


### 3. Serializing and Deserializing with XML

Explore serialization and deserialization using XML.

#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
"""Serializes a dictionary to an XML file."""
root = ET.Element("data")
for key, value in dictionary.items():
element = ET.SubElement(root, key)
element.text = str(value)

tree = ET.ElementTree(root)
tree.write(filename)


def deserialize_from_xml(filename):
"""Deserializes XML data from a file and returns a dictionary."""
try:
tree = ET.parse(filename)
root = tree.getroot()
data = {element.tag: element.text for element in root}
return data
except FileNotFoundError:
print(f"Error: File '{filename}' not found.")
return None
except Exception as e:
print(f"An error occurred: {e}")
return None

def main():
"""Main function to demonstrate serialization and deserialization."""
sample_dict = {'name': 'John', 'age': '28', 'city': 'New York'}
xml_file = "data.xml"

serialize_to_xml(sample_dict, xml_file)
print(f"Dictionary serialized to {xml_file}")

deserialized_data = deserialize_from_xml(xml_file)
print("\nDeserialized Data:")
print(deserialized_data)

if name == "main":
main()


Sample `data.xml`:

<data> <name>John</name> <age>28</age> <city>New York</city> </data> ```

General Requirements
Allowed editors: vi, vim, emacs

Ubuntu 20.04 LTS, python3 (version 3.8.5)

All files end with a new line

First line: #!/usr/bin/python3

README.md at the root

pycodestyle style (version 2.7.*)

All files executable

File length checked using wc

Python Test Cases Requirements
Allowed editors: vi, vim, emacs

All files end with a new line

Test files in tests folder

Test files as text files (extension .txt)

Tests well explained

Modules, classes, and functions documented

No from my_module import *

## Installation
Clone the repository:

git clone <repository_url>

Navigate to the project directory:
cd <project_directory>

Create and activate a virtual environment (recommended):
python3 -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows

Install requirements (if any):
pip install -r requirements.txt

## Usage
Run each task by executing its Python file:

python3 task_00_basic_serialization.py

## Contributing
Contributions are welcome!

Fork the repository.

Create a branch: git checkout -b feature/new-feature

Commit: git commit -m 'Add new feature'

Push: git push origin feature/new-feature

Create a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file.


To further shorten this, you can remove the detailed descriptions of each function and object within the task sections, focusing on the core logic and examples.  Also, feel free to remove the Resources section if space is a major concern, though I would advise keeping it.  Also make it more compact and remove unnecessary information.

