#!/usr/bin/python3
"""Defines checks for inheritance."""


def inherits_from(obj, a_class):
    """Checks for inheritance.

    Args:
        obj (any): object.
        a_class (type): class.
    Returns:
        True or False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
