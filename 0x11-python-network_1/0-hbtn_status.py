#!/usr/bin/python3
"""Fetche the url"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        byte = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(byte)))
        print("\t- content: {}".format(byte))
        print("\t- utf8 content: {}".format(byte.decode("utf-8")))
