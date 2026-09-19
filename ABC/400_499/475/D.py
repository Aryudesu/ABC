from itertools import permutations

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

primes = set(eratosthenes(10000000))
S = input()
strData = sorted(set(list(S)))
strIdx = dict()
for n in range(len(strData)):
    c = strData[n]
    strIdx[c] = n
# print(strIdx)
isOk = False
for data in permutations(range(10), len(strData)):
    if data[strIdx[S[0]]] == 0:
        continue
    res = 0
    for idx in range(len(S)):
        res = res * 10 + data[strIdx[S[idx]]]
    if res in primes:
        print(res)
        isOk = True
        break
if not isOk:
    print(-1)
