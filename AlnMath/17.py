import math

input()
A = [int(l) for l in input().split()]
result = 1
for a in A:
    result *= a // math.gcd(result, a)
print(result)
