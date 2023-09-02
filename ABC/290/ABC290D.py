import math


def calc(N, D, K):
    D = D % N
    g = math.gcd(N, D)
    if g != 1:
        NG = N // g
        k = K - 1
        tmp1 = k // NG
        tmp2 = k % NG
        return tmp1 + (tmp2 * D) % N
    else:
        return (D * (K - 1)) % N


T = int(input())
result = []
for t in range(T):
    N, D, K = [int(l) for l in input().split()]
    result.append(calc(N, D, K))
for r in result:
    print(r)
