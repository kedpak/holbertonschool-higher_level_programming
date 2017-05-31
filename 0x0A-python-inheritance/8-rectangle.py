#!/usr/bin/python3
'''module: 8-rectangle
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class: Rectangle
    '''
    def __init__(self, width, height):
        '''method: init
        '''
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "height", self.__height)
        BaseGeometry.integer_validator(self, "width", self.__width)
