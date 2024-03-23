import math


def calc(N, M, K):
    L = 1
    R = 10 ** 20
    G = math.gcd(N, M)
    Y = (N * M) // G
    while abs(L - R) > 1:
        tmp = (L + R) // 2
        num = (tmp // N) + (tmp // M) - 2 * (tmp // Y)
        check = (tmp % N == 0 and tmp % M != 0) or (tmp % N != 0 and tmp % M == 0)
        if num >= K:
            if not check:
                R = tmp + 1
                if math.gcd(R - L) == 2:
                    return L
            else:
                R = tmp
        else:
            L = tmp
    return R


N, M, K = [int(l) for l in input().split()]
print(calc(N, M, K))
