from heapq import heappush, heappop

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
PRIMES = eratosthenes(10**5)

def calc(num: int):
    pData = dict()
    n = 1
    pIdx = 0
    while True:
        p = PRIMES[pIdx]
        if p * n > num:
            break
        n *= p
        pIdx += 1
    data = []
    for idx in range(pIdx):
        heappush(data, PRIMES[idx])
    print(data)


T = int(input())
result = []
for _ in range(T):
    N, D = map(int, input().split())