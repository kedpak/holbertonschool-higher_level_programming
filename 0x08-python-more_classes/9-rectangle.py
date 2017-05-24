#!/usr/bin/python3
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
        return ("{0}({1},{2})".format("Rectangle", self.__width,
                                      self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_1.area() > rect_2.area() == 0:
            return (rect_1)
        if rect_1.area() < rect_2.area():
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        c = cls(size, size)
        return (c)
