#!/usr/bin/python3
"""Defines an sorted list."""


class MyList(list):
    """Implements in ascending order."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
