#!/usr/bin/pytnon3
class Rectangle():
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(self.__width) != int:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(self.__height) != int:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        return ((str(self.print_symbol) * self.__width + '\n') *
                (self.__height - 1) + str(self.print_symbol) * self.__width)

    def __repr__(self):
        return ("{0}({1},{2})".format
                ("Rectangle", self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
