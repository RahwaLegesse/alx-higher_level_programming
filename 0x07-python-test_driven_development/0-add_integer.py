#!/usr/bin/python3
"""Module for add_integer method."""


def add_integer(a, b=98):
    """Adds two numbers.

    Args:
        a: first number.
        b: second number.

    Raises:
        TypeError: if a and b are not either int or float.

    Returns:
        The sum of two numbers.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    elif type(b) not in (int, float):
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
