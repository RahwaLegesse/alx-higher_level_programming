#!/usr/bin/python3
"""Sends a search request for a given string to the Star Wars API."""
import sys
import requests


if __name__ == "__main__":
    url = "https://swapi.co/api/people"
    argument = {"search": sys.argv[1]}
    response = requests.get(url, argument=argument).json()

    print("Number of results: {}".format(response.get("count")))
    [print(ask.get("name")) for ask in response.get("results")]
