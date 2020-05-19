#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        var = fct(args[0], args[1])
    except (ValueError, TypeError, ZeroDivisionError, IndexError) as err:
        print("Exception:", err, file=sys.stderr)
        return None
    return var
