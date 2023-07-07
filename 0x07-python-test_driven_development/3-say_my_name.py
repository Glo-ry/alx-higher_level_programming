#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """
    Prints the name with the given first name and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If `first_name` is not a string.
        TypeError: If `last_name` is not a string.

    Returns:
        None

    Examples:
        >>> say_my_name("John", "Doe")
        My name is John Doe

        >>> say_my_name("Alice")
        My name is Alice

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
