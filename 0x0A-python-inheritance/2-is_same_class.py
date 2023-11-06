#!/usr/bin/python3
"""Defines a class that checks for instance."""


def is_same_class(obj, a_class):
    """Check if an objeject is the same.

    Args:
        obj (any): object.
        a_class (type): class.
    Returns:
        True or false.
    """
    if type(obj) == a_class:
        return True
    return False
