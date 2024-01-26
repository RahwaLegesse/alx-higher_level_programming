#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST."""

from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    data = urlencode({
                        'email': argv[2]
                    }).encode('ascii')
    ask = Request(argv[1], data)

    with urlopen(ask) as response:
        print(response.read().decode('utf-8'))
