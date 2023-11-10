#!/usr/bin/python3

"""
Write a recursive function that queries the Reddit
API and returns a list containing the titles of all
hot articles for a given subreddit. If no results are
found for the given subreddit, the function should return None.
"""


import requests


def recurse(subreddit, hot_list=[], after=''):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    req = requests.get(url, headers={'User-agent': 'Carlos'},
                       allow_redirects=False, params={'after': after})
    if req.status_code == 200:
        after = req.json().get('data').get('after')
        for posts in req.json().get('data').get('children'):
            hot_list.append(posts.get('data').get('title'))
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None
