#!/usr/bin/python3
"""
Create a Class Square with:
- size, position private propreties
- method of area and method of print_square
- getters & setters.
"""


class Square:
    """Class-Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor of a Square with the size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size private attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the size private attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the size private attribute"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(n, int) for n in value) or \
                any(n < 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Method to get the area of the Square"""
        return self.__size * self.__size

    def my_print(self):
        """Method to print a square pattern"""
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print("_", end="")
            for _ in range(self.__size):
                print("#", end="")
            print()

