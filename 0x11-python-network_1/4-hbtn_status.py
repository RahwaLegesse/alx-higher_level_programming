#!/usr/bin/python3
"""Fetches the URL:"""

import requests


if __name__ == "__main__":
    ask = requests.get('https://intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type: {_type}'.format(_type=type(ask.text)))
    print('\t- content: {_content}'.format(_content=ask.text))
