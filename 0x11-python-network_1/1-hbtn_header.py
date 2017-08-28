#!/usr/bin/python3
"""
script takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id found in header response
"""
import sys
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        headers = response.info()
        print(headers['X-Request-Id'])
