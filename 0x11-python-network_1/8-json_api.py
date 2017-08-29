#!/usr/bin/python3
"""
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.stderr.write("No Result\n")
    elif sys.argv[1].isalpha() is False or sys.argv[1].islower() is False:
        sys.stderr.write("No Result\n")
    else:
        url = "http://0.0.0.0:5000/search_user"
        req = requests.post(url, data={'q': sys.argv[1]})
        if req.headers['content-type'] != 'application/json':
            sys.stderr.write("Not a valid JSON\n")
        else:
            req = req.json()
            print("[{}] {}".format(req['id'], req['name']))
