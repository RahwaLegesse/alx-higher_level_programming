#!/usr/bin/python3
"""Defines a Rect"""


class Rectangle:
    """Represent  rect."""

    def __init__(self, w=0, h=0):
        """Initialize Rect.

        Args:
            w (int):w.
            h (int):h.
        """
        self.w = w
        self.h = h

    @property
    def w(self):
        """Get/set  width"""
        return self.__w

    @w.setter
    def w(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__w = value

    @property
    def h(self):
        """Get/set height."""
        return self.__h

    @h.setter
    def h(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__h = value

    def area(self):
        """Return area Rect."""
        return (self.__w * self.__h)

    def perimeter(self):
        """Return  perimeter."""
        if self.__w == 0 or self.__h == 0:
            return (0)
        return ((self.__w * 2) + (self.__h * 2))
