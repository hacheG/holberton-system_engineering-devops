#!/usr/bin/python3
"""i see API's everywhere"""
import requests

def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
    r = requests.get(url, headers=headers)
    print (r.status_code)
    if r.status_code == 200:
        dataJson = r.json()['data']['subscribers']
        return dataJson
    else:
        return 0
 