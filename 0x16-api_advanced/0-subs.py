#!/usr/bin/python3
"""
HOW MANY SUBSCRIBERS FUNCTION
"""

import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number
    of subscribers (not active users, total subscribers) for a
    given subreddit
    """

    if not subreddit or type(subreddit) is not str:
        return 0

    user_agent = {'User-agent': 'Devmarc.tech'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
