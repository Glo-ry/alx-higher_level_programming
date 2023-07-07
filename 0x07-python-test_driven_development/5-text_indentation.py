#!/usr/bin/python3


def text_indentation(text):
    """
    Prints the given text with 2 new lines after each occurrence
    of ".", "?", and ":" characters.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If `text` is not a string.

    Returns:
        None

    Examples:
        >>> text_indentation("Hello. How are you? I'm good.")
        Hello
        How are you

        I'm good.

        >>> text_indentation("This is a test: one, two, three.")
        This is a test

        one, two, three

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = [".", "?", ":"]
    lines = text.splitlines()

    for line in lines:
        line = line.strip()  # Remove leading/trailing spaces

        # Check if line ends with a punctuation mark
        if line.endswith(tuple(punctuation_marks)):
            print(line)
            print()
        else:
            print(line)
