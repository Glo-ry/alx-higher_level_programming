#!/usr/bin/python3

from add_0 import add

def print_sum(a, b):
    """Print the sum of a and b."""
    print("{} + {} = {}".format(a, b, add(a, b)))

if __name__ == "__main__":
    print_sum(1, 2)
