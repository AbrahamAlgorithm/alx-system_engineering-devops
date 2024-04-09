#!/usr/bin/python3
"""get a lit of suscribber on a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """number of suscribers"""
    if subreddit is None or type(subreddit) != str:
        return (0)
    url = "http://www.reddit.com/r/{}/about.json".format(
            subreddit)
    headers = {'User-Agent': 'API project'}
    response = requests.get(url, headers=headers)
    if (response.status_code != 200):
        return (0)
    sus = response.json().get("data").get('subscribers', 0)
    return (sus)
