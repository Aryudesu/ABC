from bisect import bisect_left
import random

def Miller_Rabin_test(num):
    if num == 2:
        return True
    if num > 2 and num & 1 == 0:
        return False

    s, t = 0, num-1
    while t & 1 == 0:
        s, t = s+1, t >> 1
    a = random.randint(1, num-1)
    if pow(a, t, num) == 1:
        return True
    for i in range(0, s):
        if pow(a, pow(2, i) * t, num) == num-1:
            return True
    return False

def calcNextPrime(num: int)->int:
    if num % 2 == 0:
        num += 1
    while True:
        if Miller_Rabin_test(num):
            return num
        num += 2

def calc(num: int, primes: list[int]):
    if num <= primes[-1]:
        idx = bisect_left(primes, num)
        n = primes[idx]
        return primes[idx] - num
    return calcNextPrime(num) - num
    

def eratosthenes(N: int)->list[int]:
    """エラトステネスの篩"""
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    primes = [2] if N >= 2 else []
    for i in range(3, N + 1, 2):
        if not is_prime[i]:
            continue
        primes.append(i)
        if i * i > N:
            continue
        for j in range(i * i, N + 1, 2 * i):
            is_prime[j] = False
    return primes

primes = eratosthenes(10**6+5000)
pSet = set(primes)
result = []
T = int(input())
for _ in range(T):
    N = int(input())
    result.append(calc(N, primes))
print(*result, sep="\n")
