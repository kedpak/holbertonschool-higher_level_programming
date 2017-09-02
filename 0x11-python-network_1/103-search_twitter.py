#!/usr/bin/python3
"""
Python script that takes in 3 strings.
Sends a search request to the Twitter API.
"""
import sys
import requests
import base64

if __name__ == "__main__":
    c_key = sys.argv[1]
    c_secret = sys.argv[2]
    api_keys = '{}:{}'.format(c_key, c_secret).encode('ascii')
    api_encode = base64.b64encode(api_keys)
    api_encode = api_encode.decode('ascii')

    headers = {
        'Authorization': 'Basic {}'.format(api_encode),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    data = {
        'grant_type': 'client_credentials'
    }

    url = "https://api.twitter.com/"
    auth_url = '{}oauth2/token'.format(url)
    resp = requests.post(auth_url, headers=headers, data=data)
    access_token = resp.json()['access_token']

    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    search_params = {
        'q': sys.argv[3],
        'result_type': 'recent',
        'count': 5
    }

    search_url = '{}1.1/search/tweets.json?'.format(url)
    search_resp = requests.get(search_url, headers=search_headers,
                               params=search_params)
    search_resp = search_resp.json()

    for tweet in search_resp.get('statuses'):
        print("[{}] {} by {}".format(tweet['id'], tweet['text'],
                                     tweet['user']['name']))
