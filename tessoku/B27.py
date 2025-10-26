from math import gcd

A, B = [int(l) for l in input().split()]
print(A // gcd(A, B) * B)
