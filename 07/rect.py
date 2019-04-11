#!/usr/bin/env python3
"""
Cviceni 7
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


class Matrix():
    """
    Class representing matrix
    """
    def __init__(self,values):
        self._values = values
        
    
    def __getitem__(self,i):
        return self._values[i]
        
    
    def __add__(self, other):
        suma = []
        for i in range(len(self._values)):
            row = []
            for j in range(len(self._values[0])):
                row.append(self[i][j]+other[i][j])
            suma.append(row)
        return suma

    def __repr__(self):
        return self._values.__repr__()



class Logger():
    """
    Logger
    """
    
    def __init__(self, name):
        self._name = name
    
    
    def set_level(self, level):
        self._level = level
        
    
    def log(self, level, message):
        pass
    
    def add_printer(self, printer)
        
if __name__ == "__main__":
    r = Rectangle(4,5)
    print(r.get_area())
    r.set_size(2,4)
    print(r.get_area())
