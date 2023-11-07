#!/usr/bin/python3
# 6-from_json_string.py
"""Define JSON-to-object."""
import json


def from_json_string(my_str):
    """Return Python."""
    return json.loads(my_str)
