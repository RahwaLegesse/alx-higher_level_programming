#!/usr/bin/python3
"""Func that adds attributes."""


def add_attribute(obj, att, value):
    """Add a new object.

    Args:
        obj (any): object.
        att (str): name.
        value (any): value.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
