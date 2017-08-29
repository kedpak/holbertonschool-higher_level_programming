#!/usr/bin/python3
"""
Python script that takes your Github credentials
(username and password) and uses the Github API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    url = 'https://api.github.com/user/'
    userName = sys.argv[1]
    userPswd = sys.argv[2]
    req = requests.get(url, auth=(userName, userPswd))
    req = req.json()

    try:
        print(req.get('id'))
    except:
        print("None")
