#!/usr/bin/python3
"""Module for task 1"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import requests
    import sys

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(sys.argv[1]),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        print('None')
    [print(child.get("data").get("title"))
     for child in sub_info.json().get("data").get("children")]
