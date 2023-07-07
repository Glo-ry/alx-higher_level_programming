#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list): A matrix represented as a list of lists containing
        integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If `div` is not a number (integer or float).
        ZeroDivisionError: If `div` is equal to 0.

    Returns:
        list: A new matrix with all elements divided by `div`, rounded to 2
        decimal places.
    """

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
