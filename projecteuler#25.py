# 1000-digit Fibonacci Number

import math

def numLength(n):
    return len(str(n))

x, y = 1, 1

while numLength(y) < 1000:
    x, y = y, x + y

n = y

digits = [int(digit) for digit in str(n)]

if len(digits) == 1000:
    print("The first term in the Fibonacci sequence to contain 1000 digits is:", n)
else:
    print("No term in the Fibonacci sequence contains 1000 digits.")

def add(x, y):
    return x + y
