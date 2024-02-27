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
        """Setter of position"""
        if (len(value) != 2) or (type(value) is not tuple) \
                or (type(value[0]) is not int) \
                or (type(value[1]) is not int) \
                or (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
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

