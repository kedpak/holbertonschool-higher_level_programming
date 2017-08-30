#!/usr/bin/python3
"""
10 commits (from the most recent to oldest) of
repository rails by the user rails
must use the Github API
"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/" + sys.argv[
        2] + "/" + sys.argv[1] + "/commits"
    req = requests.get(url)
    req = req.json()

    i = 0
    if len(req) >= 10:
        while (i < 10):
            print("{}: {}".format(req[i].get('sha'), req[i].get(
                'commit').get('author').get('name')))
            i += 1
    else:
        while (i < len(req)):
            print("{}: {}".format(req[i].get('sha'), req[i].get(
                'commit').get('author').get('name')))
            i += 1
