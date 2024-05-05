# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 22:40:34 2024

@author: M.SAKSHAM
GitHub: Saksham093
"""


def sieve_of_eratosthenes(max_num):
    prime = [True for _ in range(max_num+1)]
    p = 2
    while (p * p <= max_num):
        if prime[p]:
            for i in range(p * p, max_num+1, p):
                prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, max_num) if prime[p]]
    return prime_numbers


if __name__ == "__main__":
    max_range = int(input("Enter the maximum range to find prime numbers: "))
    primes = sieve_of_eratosthenes(max_range)
    print(f"Prime numbers up to {max_range} are: {primes}")


# %%

def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def sieve_of_eratosthenes(max_num):
    prime = [True for _ in range(max_num+1)]
    p = 2

    while (p * p <= max_num):
        if (prime[p]):
            for i in range(p * p, max_num+1, p):
                prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, max_num) if prime[p]]
    return prime_numbers


if __name__ == "__main__":
    max_range = int(input("Enter the maximum range to find prime numbers: "))
    primes = sieve_of_eratosthenes(max_range)
    print(f"Prime numbers up to {max_range} are: {primes}")
