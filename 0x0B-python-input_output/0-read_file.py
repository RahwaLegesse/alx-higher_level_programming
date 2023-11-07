#!/usr/bin/python3
"""Defines print using function."""


def read_file(filename=""):
    """Print out contents."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
