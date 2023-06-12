#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    index = len(my_list) - 1
    while index >= 0:
        print("{}".format(my_list[index]))
        index -= 1
