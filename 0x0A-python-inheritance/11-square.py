#!/usr/bin/python3
"""Rep a Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rep a square."""

    def __init__(self, size):
        """Initialize square.

        Args:
            size (int): size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
