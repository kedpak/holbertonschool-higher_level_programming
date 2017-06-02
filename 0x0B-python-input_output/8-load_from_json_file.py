#!/usr/bin/python3
import json
'''module 8-load_from_json_file
'''


def load_from_json_file(filename):
    '''method: load_from_json_file
    write object that creates an Object
    from a json file
    '''
    with open(filename, 'r') as f:
        z = json.load(f)
        return (z)
