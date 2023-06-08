#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

def print_operations(a, b):
    """Print the sum, difference, product, and quotient of a and b."""
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

if __name__ == "__main__":
    a = 10
    b = 5

    print_operations(a, b)
