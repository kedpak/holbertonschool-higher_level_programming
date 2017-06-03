#!/usr/bin/python3
'''module: 11-student
'''


class Student:
    '''class: Student
    defines student by first name, last name, and age
    '''
    def __init__(self, first_name, last_name, age):
        '''constructor
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''method: return dictionary representatin of attributes
        '''
        return(self.__dict__)
