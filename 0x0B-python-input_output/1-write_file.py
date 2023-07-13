#!/usr/bin/python3

"""
Contains a function that writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number
    of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        num_chars = file.write(text)
        return num_chars
