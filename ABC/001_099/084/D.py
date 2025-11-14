from atcoder.fenwicktree import FenwickTree

def calcPrimes(N: int) -> set[int]:
    result = [True] * (N + 1)
    primes = {2}
    for i in range(3, N + 1, 2):
        if not result[i]:
            continue
        primes.add(i)
        idx = 3
        while idx * i <= N:
            result[idx * i] = False
            idx += 2
    return primes

M = 10 ** 5 + 1
primes = calcPrimes(M)
ft = FenwickTree(M)
count = 0
for i in range(M):
    if i % 2 == 1:
        if (i in primes) and ((i+1) // 2 in primes):
            ft.add(i, 1)
Q = int(input())
result = []
for _ in range(Q):
    l, r = map(int, input().split())
    result.append(ft.sum(l, r + 1))
for r in result:
    print(r)
