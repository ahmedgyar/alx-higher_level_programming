#!/usr/bin/python3

"""Create a Class Square with size, method of area and getters & setters"""
class Square:
    """Class-Square"""
    def __init__(self, size=0):
        """Constructor of a Square with the size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter for the size private attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size private attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method to get the area of the Square"""
        return self.__size * self.__size
