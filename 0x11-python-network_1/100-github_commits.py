#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository."""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    ask = requests.get(url)
    response = ask.json()
    try:
        for j in range(10):
            print("{}: {}".format(
                response[j].get("sha"),
                response[j].get("commit").get("author").get("name")))
    except IndexError:
        pass
