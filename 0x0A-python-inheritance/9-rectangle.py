#!/usr/bin/python3
'''module: 9-rectangle.py
'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class: Rectangle
    '''

    def __init__(self, width, height):
        '''public method: __init__
        '''
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "height", self.__height)
        BaseGeometry.integer_validator(self, "width", self.__width)

    def area(self):
        '''public method: area
        '''
        return (self.__width * self.__height)

    def __str__(self):
        '''public method: __str__
        '''
        return ("[{0}] {1}/{2}".format(self.
                __class__.__name__, self.__width, self.__height))
