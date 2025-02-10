#!/usr/bin/python3

class Student:
    """
    A class that defines a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes name contained in this list are retrieved.
        Otherwise, all attributes are retrieved.

        Args:
            attrs (list): A list of attribute names to retrieve.

        Returns:
            dict: A dictionary containing the requested attributes or all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary where keys are attribute names and values are attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
