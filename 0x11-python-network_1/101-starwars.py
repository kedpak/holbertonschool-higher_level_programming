#!/usr/bin/python3
"""
Python script that takes in a string and sends
a search request to the Star Wars API
Manages pagination
"""

import requests
import sys

if __name__ == "__main__":
    req = requests.get('https://swapi.co/api/people/?search=' + sys.argv[1])
    req = req.json()
    print("Number of result: {}".format(req['count']))

    i = 0
    while i <= len(req['results']):
        if req['next'] is not None and i == len(req['results']):
            req2 = requests.get(req['next'])
            req = req2.json()
            i = 0
        try:
            print(req['results'][i].get('name'))
        except:
            pass
        i += 1
