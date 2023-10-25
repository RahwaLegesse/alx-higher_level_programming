#!/usr/bin/python3
"""Define a class."""


class Square:
    """Represent a function."""

    def __init__(self, size=0):
        """Initialize class.
        Args:
            size (int): size.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area."""
        return (self.__size * self.__size)
