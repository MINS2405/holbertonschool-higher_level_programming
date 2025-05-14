#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides 2 integers and prints the result.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        float: The value of the division, otherwise: None.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
