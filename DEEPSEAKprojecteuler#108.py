# Deepseak Diophantine Reciprocals I

import math
from itertools import count
from functools import reduce
import operator

def primes_up_to(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for num in range(2, int(math.sqrt(limit)) + 1):
        if sieve[num]:
            sieve[num*num : limit+1 : num] = [False] * len(sieve[num*num : limit+1 : num])
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

def minimal_n(target_solutions):
    target_divisors = 2 * target_solutions - 1
    primes = primes_up_to(100) # arbitrary limit; can be adjusted if needed
    min_n = float('inf')

    # We'll use a recursive approach to generate combinations of exponents
    def dfs(index, current_exponents, current_divisors, current_n):
        nonlocal min_n

        if current_divisors >= target_divisors:
            if current_n < min_n:
                min_n = current_n
            return

        if index >= len(primes):
            return

        prime = primes[index]
        if current_exponents:
            max_exponent = current_exponents[-1]
        else:
            max_exponent = float('inf')

        remaining_divisors = (target_divisors + current_divisors - 1) // current_divisors
        max_possible_exponent = (remaining_divisors - 1) // 2

        if max_exponent == float('inf'):
            max_exponent_to_try = max_possible_exponent
        else:
            max_exponent_to_try = min(max_possible_exponent, max_exponent)

        for e in range(max_exponent_to_try, -1, -1):
            if e == 0:
                new_exponents = current_exponents
                new_divisors = current_divisors
                new_n = current_n
            else:
                new_exponents = current_exponents + [e]
                new_divisors = current_divisors * (2 * e + 1)
                new_n = current_n * (prime ** e)

            if new_n < min_n:
                dfs(index + 1, new_exponents, new_divisors, new_n)

    dfs(0, [], 1, 1)
    return min_n

target = 4_000_000  # Increased from 1000 to 4,000,000
result = minimal_n(target)
print(result)

#target = 1000
#result = minimal_n(target)
#print(result)

print("hewo \":)\"")