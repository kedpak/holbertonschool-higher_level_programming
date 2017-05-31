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
        super().__init__(size, size)

    def __str__(self):
        '''public method: str
        '''
        return ("[Rectangle] {1}/{2}".
                format(self.__class__.__name__, self.__width, self.__height))
