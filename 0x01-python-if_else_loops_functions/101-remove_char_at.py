#!/usr/bin/python3
# 101-remove_char_at.py


def remove_char_at(string, n):
    """Create a copy of the string without the character at position n."""
    if n < 0:
        return string
    return string[:n] + string[n + 1:]

