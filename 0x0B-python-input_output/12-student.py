#!/usr/bin/python3
'''module: 12-student
'''


class Student:
    '''class: Student
    defines student by first name, last name, and age
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        if attrs is None:
            return(self.__dict__)
        if type(attrs) is list:
            for i in range(len(attrs)):
                if hasattr(self, attrs[i]) is True:
                    new_dict[attrs[i]] = getattr(self, attrs[i])
            return(new_dict)
