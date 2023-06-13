#!/usr/bin/python3
"""Define a class Square. based on 1-square.py"""


class Square:
    """
    Represent a square.
    Args:
        size (int): The size of the new square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize  square.
        """
        self.size = size  # Initialize the size of the square
        self.position = position  # Initialize the position of the square

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value  # Set the size of the square

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter

        Attribute:
            value: sets position to value if tuple is 2 integers ints
        """
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) is not int or type(value[1]) is not int
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value  # Set the position of the square

    def area(self):
        """Calculate the area of the square."""
        return (self.__size)**2

    def my_print(self):
        """Print the square with the '#' character."""
        if self.__size == 0:
            print("")  # Print an empty line if size is 0
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))
