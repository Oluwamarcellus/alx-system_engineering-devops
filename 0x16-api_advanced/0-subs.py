#!/usr/bin/python3
"""
HOW MANY SUBSCRIBERS FUNCTION
i"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number
    of subscribers (not active users, total subscribers) for a
    given subreddit
    """
    if not subreddit or type(subreddit) is not str:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, params={"User-Agent": "devmarc.tech"})
    try:
        res = res.json()
        return res.get("data", 0).get("subscribers", 0)
    except Exception:
        return 0
