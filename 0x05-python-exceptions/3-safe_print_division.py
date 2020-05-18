#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        c = None
        return c
    finally:
        print("Inside Result: {}".format(c))
