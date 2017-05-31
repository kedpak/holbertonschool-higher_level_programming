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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        self.__width = width
        self.__height = height

    def area(self):
        '''public method: area
        '''
        return (self.__width * self.__height)

    def __str__(self):
        '''public method: __str__
        '''
        return ("[Rectangle] {0}/{1}".format(self.__width, self.__height))
