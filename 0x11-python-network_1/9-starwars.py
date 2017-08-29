#!/usr/bin/python3
"""
Python script that takes in a string and sends
a search request to the Star Wars API
"""
import requests
import sys

if __name__ == "__main__":

    arr_names = []
    i = 1

    while (i < 89):
        req = requests.get('https://swapi.co/api/people/' + str(i) + '/')
        req = req.json()

        if 'name' not in req:
            """some id's from the api are empty, this conditons takes
            care of empty dicts"""
            i += 1
            continue
        if sys.argv[1].lower() in req['name'].lower():
            arr_names.append(req['name'])
        i += 1

    print("Number of result: {}".format(len(arr_names)))
    for v in arr_names:
        print(v)
