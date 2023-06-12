#!/usr/bin/python3
# 7-add_tuple.py


def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples."""
    tuple_a = tuple_a[:2] + (0, 0)[:2 - len(tuple_a)]
    tuple_b = tuple_b[:2] + (0, 0)[:2 - len(tuple_b)]
    return tuple(map(sum, zip(tuple_a, tuple_b)))
