#!/usr/bin/pytnon3
class Rectangle():
    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise TypeError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value
