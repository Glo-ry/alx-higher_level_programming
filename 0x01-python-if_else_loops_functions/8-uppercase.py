#!/usr/bin/python3
# 8-uppercase.py

def uppercase(string):
    """Print a string in uppercase."""
    for c in string:
        if 'a' <= c <= 'z':
            c = chr(ord(c) - 32)
        print(c, end="")
    print("")
