import math


def calc(N, M):
    N, M = [int(l) for l in input().split()]
    for n in range(1, N + 1):
        t = int('1'*n)
        g = math.gcd(t, M)
        tmp = M // g
        if tmp < 10:
            return t
    return -1


nlen = 0
Num = [9, 8, 7, 6, 5, 4, 3, 2, 1]
