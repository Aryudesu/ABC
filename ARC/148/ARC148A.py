import math

N = int(input())
A = [int(l) for l in input().split()]
res = 0
for i in range(N):
    res = math.gcd(res, A[i] - A[0])
print(1 if res - 1 else 2)
