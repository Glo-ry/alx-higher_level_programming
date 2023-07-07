#!/usr/bin/pythion3


def add_integer(a, b=98):
    """Add two integers.

    Adds two integers `a` and `b` and returns their sum.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float.
        Defaults to 98.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.

    Returns:
        int: The sum of `a` and `b` as an integer.
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
