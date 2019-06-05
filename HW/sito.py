#!/usr/bin/env python3


import math


def find_primes1(n):
    primes = {x for x in range(2,n+1)}
    max_sqrt = int(math.sqrt(n))
    for i in range(2,max_sqrt+1):
        for j in range(2*i,n+1,i):
            if j in primes:
                primes.remove(j)
    print(len(primes))


def find_primes(n):
    """
    Returns number of primes
    """
    is_prime = [True]*n
    for i in range(3,int(math.sqrt(n))+1,2):
        if is_prime[i]:
            for j in range(i*i,n+1,2*i):
                is_prime[j] = False
            #is_prime[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    print(len([2] + [i for i in range(3,n,2) if is_prime[i]]))

if __name__ == "__main__":
    n = int(input())
    find_primes1(n)
