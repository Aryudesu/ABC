import math

A, B, C = [int(l) for l in input().split()]

g = math.gcd(A, math.gcd(B, C))
print(A//g + B//g + C//g - 3)
