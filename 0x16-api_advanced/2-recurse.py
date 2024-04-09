#!/usr/bin/python3
"""add to a list of hot list"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """recurse the value"""
    params = {
        'after': after,
        'count': count,
        'limit': 100
    }
    headers = {'User-Agent': 'Alx Task'}
    url = 'http://www.reddit.com/r/{}/top/.json'.format(subreddit)
    res = requests.get(url, params=params,
                       headers=headers)
    if res.status_code >= 400:
        return None
    result = res.json().get('data')
    after = result.get('after')
    count += result.get('dist')
    resp = result.get('children')
    for child in resp:
        hot_list.append(child.get('data').get('title'))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    else:
        return hot_list
