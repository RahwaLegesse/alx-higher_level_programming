#!/usr/bin/python3
"""Define a class function."""


class Square:
    """Represent a class."""

    def __init__(self, size=0):
        """Initialize function.
        Args:
            size (int): size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area."""
        return (self.__size * self.__size)
