#!/usr/bin/env python3
"""
Check whether the string is palindrome
"""


def je_palindrom(slovo):
    reverse = slovo[::-1]
    if slovo == reverse:
        return True
    return False

if __name__ == "__main__":
    print(je_palindrom("radar"))
    
