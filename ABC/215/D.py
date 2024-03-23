def calc_primes(N):
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



N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
data = [True] * (M + 1)
primes = calc_primes(M)
for a in A:
    for p in primes:
        if not data[p]:
            continue
        if p > a:
            break
        if a % p == 0:
            for idx in range(p, M + 1, p):
                data[idx] = False
result = []
for idx in range(1, M + 1):
    if data[idx]:
        result.append(idx)
print(len(result))
for r in result:
    print(r)
