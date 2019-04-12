#!/usr/bin/env python3
"""
Range
"""


def my_range(start=0,end,step=1):
    if end > start and step < 0:
        return
    if end < start and step > 0:
        return
    i = start
    while i < end:
        yield i
        i+=step


if __name__ == "__main__":
    for x in my_range(10,1,-1):
        print(x)
    
