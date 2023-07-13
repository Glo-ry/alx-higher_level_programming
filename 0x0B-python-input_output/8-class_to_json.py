#!/usr/bin/python3

"""
Contains a function that returns the dictionary description
with simple data structure
"""


def class_to_json(obj):
    """
    Return the dictionary description of an object with a simple data
    structure for JSON serialization

    """
    return obj.__dict__
