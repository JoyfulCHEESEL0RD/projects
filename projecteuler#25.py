# 1000-digit Fibonacci Number

import math

n = []
n = (n-1) + (n-2)


def numLength(n):
    return len(str(n))
digits = [int(digit) for digit in str(n)]

if digits == 1000:
    print("The first term in the Fibonacci sequence to contain 1000 digits is:", n)
else:
    print("No term in the Fibonacci sequence contains 1000 digits.")

def add(x, y):
    return x + y