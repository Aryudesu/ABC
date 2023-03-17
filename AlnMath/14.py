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


def soinsu(N, primes):
    """Nの素因数分解"""
    tmp = N
    idx = 0
    result = []
    while tmp > 1:
        p = primes[idx]
        if tmp % p == 0:
            while True:
                if tmp % p != 0:
                    break
                result.append(p)
                tmp //= p
        elif p * p > tmp:
            result.append(tmp)
            return result
        idx += 1
    return result


primes = calc_prime(10000000)
N = int(input())
print(*soinsu(N, primes))
