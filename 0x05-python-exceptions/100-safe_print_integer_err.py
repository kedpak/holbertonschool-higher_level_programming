#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value), file=sys.stderr)
        return (True)
    except (ValueError, TypeError):
        return (False)
