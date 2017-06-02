#!/usr/bin/python3
import sys
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
'''module: 9-add-item
'''

filename = "add_item.json"


'''add all input arguments to a list and save to file
'''
if os.path.isfile(filename):
    load = load_from_json_file(filename)
    input_items = ""
    for i in range(len(sys.argv)):
        if i > 0:
            input_items = str(sys.argv[i])
            load.append(input_items)
        save_to_json_file(load, "add_item.json")
else:
    item_list = []
    input_items = ""
    for i in range(len(sys.argv)):
        if i > 0:
            input_items = str(sys.argv[i])
            item_list.append(input_items)
        save_to_json_file(item_list, "add_item.json")
        load_from_json_file("add_item.json")
