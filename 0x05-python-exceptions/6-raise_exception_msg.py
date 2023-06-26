#!/usr/bin/python3


def raise_exception_msg(message=""):
    """
    Raise a NameError exception with a message.
    """
    try:
        raise NameError(message)
    except NameError as err:
        raise err
