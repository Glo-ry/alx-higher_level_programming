#!/usr/bin/python3

def safe_print_list_integers(my_list=[], m=0):
    """Print the first m elements of a list that are integers.

    Args:
        my_list (list): The list to print elements from.
        m (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for l in range(0, m):
        try:
            if isinstance(my_list[l], int):
                print("{:d}".format(my_list[l]), end="")
                ret += 1
        except IndexError:
            break
    print("")
    return ret

