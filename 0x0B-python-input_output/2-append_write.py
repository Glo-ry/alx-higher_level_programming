#!/usr/bin/python3

"""
Contains a function that appends a string to the end of a text file
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8) and returns
    the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        num_chars = file.write(text)
        return num_chars
