#!/usr/bin/python3
"""
count the words in a given subreddit reddit post

"""

import requests


def number_of_subscribers(subreddit):

    """Return the total number of subscribers on a given subreddit."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        mydata = response.json()
        subscribers = mydata['mydata']['subscribers']
        return subscribers
    else:
        return 0
