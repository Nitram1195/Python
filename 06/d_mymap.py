#!/usr/bin/env python3
"""
My map
"""


def my_map(f,pole):
    return [f(prvek) for prvek in pole]


if __name__ == "__main__":
   print(my_map(lambda x: x[::-1],["one","two","three"])) 
