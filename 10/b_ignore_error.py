#!/usr/bin/env python3


def ignore_errors(f):
    def inner(a, b):
        try:
            return f(a, b)   #tady musi byt return
        except ZeroDivisionError:
            return 0
    return inner


@ignore_errors
def divide(a, b):
    return a / b 

if __name__ == "__main__":
    print(divide(2,3))
    print(divide(3,0))
