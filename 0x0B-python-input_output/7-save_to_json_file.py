#!/usr/bin/python3
import json
'''module: 7-save_to_json_file
'''


def save_to_json_file(my_obj, filename):
    '''method: save_to_json_file
    method writes an object to text file, using
    JSON representation
    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
