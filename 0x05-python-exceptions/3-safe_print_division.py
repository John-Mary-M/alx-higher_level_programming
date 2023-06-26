#!/usr/bin/python3


def safe_print_division(a, b):
    '''
    Divides two integers
    '''
    inside_result = None
    try:
        inside_result = (a/b)
        return inside_result
    except:
        return None
    finally:
        quotient = inside_result
        print('{}'.format(quotient))
