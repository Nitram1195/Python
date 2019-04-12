#!/usr/bin/env python3
"""
Generator
"""


def fibonachi_gen(n):
    yield 1
    x = 0
    y = 1
    for i in range (n):
        z = x+y
        yield z
        x,y = y,z    

if __name__ == "__main__":
    for x in fibonachi_gen(10):
       print(x)
