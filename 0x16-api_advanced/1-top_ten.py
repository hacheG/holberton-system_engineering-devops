#!/usr/bin/python3
"""i see API's everywhere"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        for req in range(10):
            dataJson = r.json()['data']['children'][req]['data']['title']
            print (dataJson)
    else:
        print ("None")
