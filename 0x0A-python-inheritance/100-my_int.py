#!/usr/bin/python3
"""Defines class MyInt."""


class MyInt(int):
    """Reverse int operators == and !=."""

    def __eq__(self, value):
        """Reverse the value."""
        return self.real != value

    def __ne__(self, value):
        """Take the value itself."""
        return self.real == value
