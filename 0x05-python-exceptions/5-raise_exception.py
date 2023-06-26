def raise_exception():
    """
    Raise a TypeError exception.
    """
    try:
        1 + '1'
    except TypeError as err:
        raise err
