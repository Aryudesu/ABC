from itertools import combinations
from math import gcd

def lcm(a: int, b: int)-> int:
    return (a * b) // gcd(a, b)

N, M, Y = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
data = [l for l in range(N)]
result = 0
sgn = 1
for i in range(M, N + 1):
    for bits in combinations(data, i):
        l = A[bits[0]]
        for b in bits:
            l = lcm(l, A[b])
        print(bits, l, Y // l)
        if sgn > 0:
            result += Y // l
        else:
            result -= Y // l
    sgn = -sgn
print(result)
