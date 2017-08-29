#!/usr/bin/python3
"""
Python script that takes in a string and sends
a search request to the Star Wars API
"""
import requests
import sys

if __name__ == "__main__":

    req = requests.get('https://swapi.co/api/people/?search=' + sys.argv[1])
    req = req.json()
    print("Number of result: {}".format(req['count']))
    for name in req['results']:
        print(name['name'])
