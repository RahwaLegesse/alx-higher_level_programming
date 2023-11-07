#!/usr/bin/python3
"""Defines a append function."""


def append_write(filename="", text=""):
    """Appends a string.

    Args:
        filename (str): filename.
        text (str): string.
    Returns:
        number of characters.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
