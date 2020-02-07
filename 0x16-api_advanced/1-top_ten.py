#!/usr/bin/python3
"""i see API's everywhere"""
import requests


def top_ten(subreddit):
    final = 10
    url = 'https://www.reddit.com/r/{}/hot.json?limit={}'.format(subreddit, final)
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        dataJson = r.json()['data']['children']
        for req in dataJson:
            dataTitle = req['data']['title']
            print (dataTitle)
    else:
        print ("None")