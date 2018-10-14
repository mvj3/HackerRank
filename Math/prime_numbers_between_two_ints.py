#!/bin/python3

"""
getting prime numbers between 2 ints n and m
"""

import math

def get_prime_numbers__default(m, n):
    def is_prime(num):
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, math.floor(num/2), 2):
            if num % i == 0:
                return False
        return True

    prime_numbers_cache = []
    for i in range(n):
        if is_prime(i):
            prime_numbers_cache.append(i)
    return list(filter(lambda i: i>= m, prime_numbers_cache))


def get_prime_numbers__improved(m, n):
    def is_prime(num):
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(num) + 1), 2):
            if num % i == 0:
                return False
        return True

    prime_numbers_cache = []
    for i in range(n):
        if is_prime(i):
            prime_numbers_cache.append(i)
    return list(filter(lambda i: i>= m, prime_numbers_cache))


get_prime_numbers = get_prime_numbers__improved
print(get_prime_numbers(2, 100))
