#! usr/bin/python3
"""IT fetches the given Url"""
import urllib.request

if __name__ = "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(type(boby)))
        print("\t- utf8 content: {}".format(type(body.decode(utf8)))
