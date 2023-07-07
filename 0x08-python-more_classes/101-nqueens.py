#!/usr/bin/python3

"""Solves the N-queens puzzle.

This determines all possible solutions to NxN chessboard.

N must be an integer greater than or equal to 4.

Attributes:
    chessboard (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where
a queen must be placed on the chessboard.
"""

import sys


def initialize_chessboard(n):
    """Initialize an `n`x`n` sized chessboard with empty squares.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list: The initialized chessboard.
    """
    chessboard = [[' '] * n for _ in range(n)]
    return chessboard


def deepcopy_chessboard(chessboard):
    """Return a deep copy of a chessboard.

    Args:
        chessboard (list): The chessboard to be copied.

    Returns:
        list: The copied chessboard.
    """
    return [row.copy() for row in chessboard]


def get_solution(chessboard):
    """Return the list of lists representation of a solved chessboard.

    Args:
        chessboard (list): The chessboard containing the solution.

    Returns:
        list: The list of lists representation of the solution.
    """
    solution = []
    for r in range(len(chessboard)):
        for c in range(len(chessboard)):
            if chessboard[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def mark_unavailable_spots(chessboard, row, col):
    """Mark the spots on the chessboard where non-attacking queens
    cannot be placed.

    Args:
        chessboard (list): The current working chessboard.
        row (int): The row where a queen was last placed.
        col (int): The column where a queen was last placed.
    """
    n = len(chessboard)
    # Mark all forward spots
    for c in range(col + 1, n):
        chessboard[row][c] = "x"
    # Mark all backward spots
    for c in range(col - 1, -1, -1):
        chessboard[row][c] = "x"
    # Mark all spots below
    for r in range(row + 1, n):
        chessboard[r][col] = "x"
    # Mark all spots above
    for r in range(row - 1, -1, -1):
        chessboard[r][col] = "x"
        # Mark all spots diagonally down to the right
    for r, c in zip(range(row + 1, n), range(col + 1, n)):
        chessboard[r][c] = "x"
    # Mark all spots diagonally up to the left
    for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        chessboard[r][c] = "x"
    # Mark all spots diagonally up to the right
    for r, c in zip(range(row - 1, -1, -1), range(col + 1, n)):
        chessboard[r][c] = "x"
    # Mark all spots diagonally down to the left
    for r, c in zip(range(row + 1, n), range(col - 1, -1, -1)):
        chessboard[r][c] = "x"


def solve_nqueens(chessboard, row, queens, solutions):
    """Recursively solve the N-queens puzzle.

    Args:
        chessboard (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists to store the solutions.

    Returns:
        list: A list of lists containing all solutions.
    """
    n = len(chessboard)

    if queens == n:
        solutions.append(get_solution(chessboard))
        return solutions

    for col in range(n):
        if chessboard[row][col] == " ":
            temp_chessboard = deepcopy_chessboard(chessboard)
            temp_chessboard[row][col] = "Q"
            mark_unavailable_spots(temp_chessboard, row, col)
            solutions = solve_nqueens(
                    temp_chessboard, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_chessboard(n)
    solutions = solve_nqueens(chessboard, 0, 0, [])
    for sol in solutions:
        print(sol)
