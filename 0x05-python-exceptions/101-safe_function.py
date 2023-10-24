#!/usr/bin/python3
import sys


def safe_function(fact, *arg):
    try:
        number = fact(*arg)
        return number
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
