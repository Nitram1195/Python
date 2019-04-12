#!/usr/bin/env python3
"""
Password
"""

def heslo(delka, spec_ch = 0):
    import random
    ch = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = "!@#$%^&*()?"
    heslo =  [random.choice(ch) for i in range(delka-spec_ch)] + [random.choice(s) for i in range(spec_ch)]
    random.shuffle(heslo)
    return "".join(heslo)


if __name__ == "__main__":
    print(heslo(6,2))
