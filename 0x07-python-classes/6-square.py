#!/usr/bin/python3
class Square():
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive \
integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        return (self.__size**2)

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return (self.__position)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
        for k in range(self.__position[1]):
            if self.__position[1] > 0:
                print(" ", end="")
            print("")
        for i in range(self.__size):
            for m in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
