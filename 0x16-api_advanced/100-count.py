#!/usr/bin/python3
"""
parses the title of all hot articles,
and prints a sorted count of given keywords
"""

import requests
import re
from collections import defaultdict


def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Recursively count the number of occurrences of each word
    from word_list in the hot articles of the given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): A list of case-insensitive words to search for.
        after (str, optional): The fullname of a reddit thing.
        Used for pagination.
        word_counts (defaultdict, optional):
        A defaultdict to store the word counts.

    Returns:
        defaultdict: A defaultdict containing the word counts.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
    except (requests.exceptions.RequestException, ValueError, KeyError):
        return defaultdict(int)
    # Return an empty defaultdict if an error occurs

    if word_counts is None:
        word_counts = defaultdict(int)

    for child in data["data"]["children"]:
        title = child["data"]["title"]
        for word in word_list:
            count = len(re.findall(fr'\b{word}\b', title, re.IGNORECASE))
            word_counts[word.lower()] += count

    after = data["data"].get("after", None)
    if after:
        count_words(subreddit, word_list, after, word_counts)

    return word_counts


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [x for x in sys.argv[2].split()]
        word_counts = count_words(subreddit, word_list)

        sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")
