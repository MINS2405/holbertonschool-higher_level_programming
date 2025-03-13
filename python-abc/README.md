# Python - Abstract Classes and Interfaces

This project is part of the Python - Abstract Classes and Interfaces course at Holberton School. It covers various aspects of object-oriented programming (OOP) in Python, including abstract classes, interfaces, duck typing, and subclassing standard base classes.

## Objectives

- Understand and apply abstract classes to define common interfaces while enforcing certain levels of class completeness.
- Grasp the concept of interfaces and duck typing to ensure that objects adhere to a specific contract or protocol.
- Learn to extend standard base classes like lists, dictionaries, and iterators to create custom data structures with specialized behavior.
- Employ method overriding to alter or enhance the behavior of base class methods.
- Understand and apply multiple inheritance to form complex relationships between classes.
- Utilize mixins to compose behavior across unrelated classes.

## Tasks

1. **Abstract Animal Class and its Subclasses** : Create an abstract class `Animal` with an abstract method `sound`. Implement two subclasses: `Dog` and `Cat`.
2. **Shapes, Interfaces, and Duck Typing** : Design an abstract class `Shape` with methods `area` and `perimeter`. Implement concrete classes `Circle` and `Rectangle`. Write a function `shape_info` that uses duck typing to handle shapes uniformly.
3. **Extending the Python List with Notifications** : Create a class `VerboseList` that extends the Python list class. Override methods to print notifications when items are added or removed.
4. **CountedIterator - Keeping Track of Iteration** : Develop a class `CountedIterator` that extends the built-in iterator. It should keep track of the number of items iterated over.
5. **The Enigmatic FlyingFish - Exploring Multiple Inheritance** : Construct a `FlyingFish` class that inherits from both `Fish` and `Bird`. Override methods from both parents to demonstrate multiple inheritance.
6. **The Mystical Dragon - Mastering Mixins** : Design mixin classes `SwimMixin` and `FlyMixin`. Create a `Dragon` class that inherits from both mixins to show modular behavior composition.

## Execution

To run the files, ensure you have Python 3 installed on your system. Use the command `python3` to execute each Python file.

## Authors

- https://github.com/MINS2405/holbertonschool-higher_level_programming/
## License

This project is under the MIT License.

