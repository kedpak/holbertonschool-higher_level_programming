#!/usr/bin/python3
'''module: 3-is_kind_of_class
'''


def inherits_from(obj, a_class):
    '''method: inherits_from
    '''
    if (issubclass(a_class, type(obj))):
        return (False)
    else:
        return (True)
