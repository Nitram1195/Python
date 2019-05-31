#!/usr/bin/env python3


class Meta(type):
    def __new__(cls, name, bases, dct):
        setattr(cls, "neco", 3)
        def struct_init(self, x = dct['x'], y = dct['y']):
             self.x = x
             self.y = y
             setattr(self, 'se', 3)
        dct['__init__'] = struct_init
        dct['a'] = 9
        x = super().__new__(cls, name, bases, dct)
        print(cls)
        print(name)
        print(bases)
        print(dct)
        return x


class MojeTrida(metaclass = Meta):
    x = 2
    y = 3


m = MojeTrida(x = 7)
print(m.x)
print(m.y)
