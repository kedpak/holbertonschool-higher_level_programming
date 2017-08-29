#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":

    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t - type: {}".format(type(req.content.decode("utf8"))))
    print("\t - content: {}".format(req.content.decode("utf8")))
