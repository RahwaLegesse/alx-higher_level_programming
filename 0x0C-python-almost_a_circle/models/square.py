square.py
#!/usr/bin/python3
"""Represents a square of the class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents class of the square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the new class of square.

        Args:
            size (int): Square size.
            x (int): x value.
            y (int): y value.
            id (int): id.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the inherited new class of Square.

        Args:
            *args (ints): given vaues.
                - 1st parameter represents id
                - 2nd parameter represents size
                - 3rd parameter represents x
                - 4th parameter represents y
            **kwargs (dict): with the key and theier respective values.
        """
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1

        elif kwargs and len(kwargs) != 0:
            for ke, val in kwargs.items():
                if ke == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif ke == "size":
                    self.size = val
                elif ke == "x":
                    self.x = val
                elif ke == "y":
                    self.y = val

    def to_dictionary(self):
        """Return dictionary."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
