#!/usr/bin/env python


class Structure:
    _fields = []
    def __init__(self, *args):
        for name, val in zip(self._fields, args):
            setattr(self, name, val)


class Point(Structure):
    _fields = ['x', 'y']
