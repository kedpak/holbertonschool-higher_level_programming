#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
        result = result + 0.0
        print("Inside result: {:.1f}".format(result))
    except ArithmeticError:
        print("Inside result: {0}".format(None))
        return None
    finally:
        return (result)
