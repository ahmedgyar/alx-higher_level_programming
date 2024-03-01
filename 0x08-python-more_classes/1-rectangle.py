#!/usr/bin/python3
"""Module to define a class Rectangle."""

class Rectangle:
    """Class that represents a rectangle.
    
    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """
    
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.
        
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        
        Args:
            value (int): The new width of the rectangle.
            
        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
        
        Args:
            value (int): The new height of the rectangle.
            
        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value