#!/usr/bin/python3


def raise_exception():
    """
    Raise a TypeError exception.
    """
    try:
        raise TypeError
    except TypeError as err:
        raise err
