#!/usr/bin/python3
"""
LIST OF TITLES OF HOT POSTS
"""
import requests


after = None


def recurse(subreddit, hot_list=[]):
    """
    recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given
    subreddit. If no results are found for the given subreddit,
    the function should return None.
    """
    global after

    if not subreddit:
        return None

    user_agent = {'User-Agent': 'Devmarc.tech'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}
    res = requests.get(
            url,
            params=params,
            headers=user_agent,
            allow_redirects=False
            )

    if res.status_code == 200:
        after_data = res.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = res.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)
