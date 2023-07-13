#!/usr/bin/python3

"""
Contains  a function that inserts a line of text to a file,
after each line containing a specific string

"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a specific
    string in a file
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
