import math


def calc_prime(N):
    """素数表作成"""
    result = [True] * (N + 1)
    primes = [2]
    for i in range(3, N + 1, 2):
        if not result[i]:
            continue
        primes.append(i)
        idx = 3
        while idx * i <= N:
            result[idx * i] = False
            idx += 2
    return primes


def totient(N, primes):
    """φ(N)の計算"""
    tmp = N
    idx = 0
    result = N
    count = 0
    while tmp > 1:
        p = primes[idx]
        if tmp % p == 0:
            count = 0
            while True:
                if tmp % p != 0:
                    break
                count += 1
                tmp //= p
        elif p * p > tmp:
            break
        idx += 1
    return result


A, X, M = [int(l) for l in input().split()]
tmp1 = (pow(A, X, M) - 1) % M
# 素数表計算
primes = calc_prime(100000)
G = math.gcd(A, M)
# トーシェント関数
tot = totient(M, primes)
print((tmp1 * (G * pow(A//G, tot, M//G))) % M)
