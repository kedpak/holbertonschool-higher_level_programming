#!/usr/bin/python3
'''module: 11-square
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
        super().__init__(size, size)
