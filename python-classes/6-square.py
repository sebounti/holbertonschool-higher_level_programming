#!/usr/bin/python3
"""Define a class Square. based on 1-square.py"""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square.
        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square.
        """
        self.__size = size  # Initialize the size of the square
        self.__position = position  # Initialize the position of the square

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
            self.__size = value  # Set the size of the square

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value  # Set the position of the square

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the '#' character."""
        if self.__size == 0:
            print()  # Print an empty line if size is 0
            return\

        for x in range(self.__position[1]):
            print()
            # Print empty lines before the square

        for x in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
            # Print the lines of the square
