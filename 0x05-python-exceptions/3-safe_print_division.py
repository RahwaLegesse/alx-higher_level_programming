#!/usr/bin/python3
def safe_print_division(x, y):
    try:
        divis = x / y
    except (ZeroDivisionError):
        divis = None
    finally:
        print("Inside result: {}".format(divis))
        return divis
