import math


def calc_primes():
    N = 2*(10**6)
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


primes = calc_primes()
A, B = [int(l) for l in input().split()]
g = math.gcd(A, B)
a, b = A//g, B//g
a, b = (a, b) if a > b else (b, a)
result = 0
while a > 0 and b > 0:
    ab = a - b
    tp = 1
    for p in primes:
        if p * p > ab:
            break
        if ab % p == 0:
            tp = p
            break
    br = ab // tp
    r = b - br
    a, b = (a-b), b - r
    result += r
print(r)
