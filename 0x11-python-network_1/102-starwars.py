#!/usr/bin/python3
"""
Python script that takes in a string and sends a
search request to the Star Wars API
displays movies that character appeared in
"""
import requests
import sys

if __name__ == '__main__':
    req = requests.get('https://swapi.co/api/people/?search=' + sys.argv[1])
    req = req.json()
    print("Number of results: {}".format(req['count']))

    i = 0
    while i <= len(req['results']):
        if req['next'] is not None and i == len(req['results']):
            req2 = requests.get(req['next'])
            req = req2.json()
            i = 0
        try:
            print(req['results'][i].get('name'))
            for j in req['results'][i].get('films'):
                req2 = requests.get(j).json()
                print("\t{}".format(req2['title']))
        except:
            pass
        i += 1
