#!/usr/bin/env python3
"""
Eratosthenovo sito
"""


import math


def find_primes(n):
    """
    Returns number of primes
    """
    is_prime = [True] * n
    for i in range(3, int(math.sqrt(n))+1, 2):
        if is_prime[i]:
            for j in range(i*i, n, 2 * i):
                is_prime[j] = False
    pocet = 1
    for i in range(3, n, 2):
        if is_prime[i]:
            pocet += 1
    print(pocet)


if __name__ == "__main__":
    MAX = int(input())
    find_primes(MAX)
