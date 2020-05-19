#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        var = fct(*args)
    except (ValueError, TypeError, ZeroDivisionError, IndexError) as err:
        print("Exception:", err, file=sys.stderr)
        return None
    return var
