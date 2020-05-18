#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a/b
    except ZeroDivisionError:
        c = None
    finally:
        print("Inside Result: {}".format(c))
    return c
