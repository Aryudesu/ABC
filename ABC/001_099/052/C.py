from collections import defaultdict

def makeData(N: int, primes: list[int]) -> list[int]:
    result = [1, 1]
    for i in range(2, N + 1):
        for p in primes:
            if i % p == 0:
                result.append(p)
                break
    return result

def getPrimes(N) -> list[int]:
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

def calc(N: int, M: int = 1005, mod: int = 1000000007):
    primes = getPrimes(M)
    pData = makeData(N, primes)
    data = defaultdict(int)
    for n in range(N + 1):
        num = n
        while num > 1:
            data[pData[num]] += 1
            num = num // pData[num]
    result = 1
    for k in data:
        result = (result * (data[k] + 1)) % mod
    return result


N = int(input())
print(calc(N, N + 5))
