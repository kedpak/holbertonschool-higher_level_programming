#!/usr/bin/python3
'''module: 10-square
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class: Square
    '''

    def __init__(self, size):
        '''public method: init
        '''
        self.__size = size
        self.__width = size
        self.__height = size

    def __str__(self):
        '''public method: str
        '''
        return ("[Rectangle] {0}/{1}".format(self.__width, self.__height))

    def area(self):
        '''public method: area
        '''
        return (self.__height * self.__width)
