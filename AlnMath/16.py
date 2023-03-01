import math

input()
A = [int(l) for l in input().split()]
result = A[0]
for a in A:
    result = math.gcd(result, a)
print(result)
