#!usr/bin/python3

"""sends a request to the URL and displays the value of the X-Request-Id

usage:./1-hbtn_header.py
"""
import sys
import urllib.request

if __name__ == __main__:
    url = sys.argv[1]
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("x-Request-id"))
