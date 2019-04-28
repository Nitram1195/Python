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


    def __eq__(self, other):
        if self.get_area() == other.get_area():
            return True
        return False


if __name__ == "__main__":
    r1 = Rectangle(1,4)
    r2 = Rectangle(2,2)
    print(r1 == r2)
