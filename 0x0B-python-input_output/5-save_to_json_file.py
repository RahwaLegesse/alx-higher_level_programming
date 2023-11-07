#!/usr/bin/python3
"""Define JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Write obj to a text file."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
