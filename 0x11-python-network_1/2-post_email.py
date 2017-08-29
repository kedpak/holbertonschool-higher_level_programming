#!/usr/bin/python3
"""
script that takes in a URL and an email,
sends a POST request to the passed URL with the email as parameter,
displays the body of the response
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    email = urllib.parse.urlencode(dict(
        {'email': sys.argv[2]})).encode('utf-8')
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req, email) as response:
        body = response.read()
        print(body.decode("utf-8"))
