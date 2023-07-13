#!/usr/bin/python3

"""
A Function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): Name of the file to read (default: "").
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
