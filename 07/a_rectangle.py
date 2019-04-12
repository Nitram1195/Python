#!/usr/bin/env python3
"""
Rectangle
"""


class Rectangle():
    """
    Class representing rectangle
    """
    def __init__(self, a = 0, b = 0):
        self._a = a
        self._b = b
    
    
    def get_area(self):
        return self._a*self._b

    def set_size(self, a, b):
        self._a = a
        self._b = b        

