#!/usr/bin/python3
'''module: 10-class_to_json
'''


def class_to_json(obj):
    '''return dictionary description with simple data structure
    for json serialization of object
    '''
    return (obj.__dict__)
