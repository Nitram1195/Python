#!/usr/bin/env python3


def prefix(class_):
    print("Methods: ")
    metody = list(vars(class_))
    public_metody = [x for x in metody if x[0] != "_"]
    print(*public_metody, sep = "\n")


@prefix
class A():


    def __init__(self):
        self._a = "a"


    def _private_f(self):
        pass


    def print_a(self):
        print(self._a)


    def set_a(self, a):
        _a = a
