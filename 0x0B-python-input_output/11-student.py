#!/usr/bin/python3

"""
Contains a class Student that defines a student
"""


class Student:
    """
    A class that represents a student

    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance

        """
        if attrs is None:
            attrs = self.__dict__.keys()
        else:
            attrs = [attr for attr in attrs if hasattr(self, attr)]

        serialized = {attr: getattr(self, attr) for attr in attrs}
        return serialized

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student

        """
        for attr, value in json.items():
            setattr(self, attr, value)
