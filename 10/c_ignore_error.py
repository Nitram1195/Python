#!/usr/bin/env python3


import functools

def ignore_errors(return_value):
    def internal_ignore_errors(f):
        @functools.wraps(f)
        def inner(a, b):
            try:
                return f(a, b)
            except ZeroDivisionError:
                return return_value
        return inner
    return internal_ignore_errors
    

@ignore_errors(2)
def divide(a, b):
    return a / b 

if __name__ == "__main__":
    print(divide(2,3))
    print(divide(3,0))
