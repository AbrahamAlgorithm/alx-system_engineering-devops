#!/usr/bin/python3
"""gets the top ten subbredit api"""
import requests


def top_ten(subreddit):
    """lists top 10 reddit api"""
    if subreddit is None or type(subreddit) != str:
        print('None')
        return
    params = {'limit': 10}
    headers = {'User-Agent': 'Reddit apI'}
    url = "http://www.reddit.com/r/{}/top/.json".format(subreddit)
    res = requests.get(url, params=params,
                       headers=headers)
    if res.status_code != 200:
        print('None')
        return
    resp = res.json().get('data').get('children')
    for child in resp:
        print(child.get('data').get('title'))
