#!/usr/bin/python3
"""Defines a ass that checks for inherited"""


def is_kind_of_class(obj, a_class):
    """Check if an object is inherited or instantaneous.

    Args:
        obj (any): object.
        a_class (type): class.

    Returns:
        If obj is an instance or inherited.
    """
    if isinstance(obj, a_class):
        return True
    return False
