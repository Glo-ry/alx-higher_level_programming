#!/usr/bin/python3

import sys

def calculate_sum():
    """Calculate the sum of all arguments."""
    total = sum(int(arg) for arg in sys.argv[1:])
    return total

if __name__ == "__main__":
    print(calculate_sum())
