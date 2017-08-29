#!/usr/bin/python3
"""
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data={'q' : sys.argv[1]})
    data_str = req.content.decode("utf8")
    data_str = data_str.replace('{', "").replace('}', "").replace(
        '\n', "").replace(' ', "")
    dic2 = dict(item.split(':') for item in data_str.split(','))
    print("[{}] {}".format(dic2['"id"'], dic2['"name"'].strip('"')))
