from bisect import bisect_left, bisect_right

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


primes = eratosthenes(10 ** 12 + 3)
L, R = map(int, input().split())
l_num = bisect_left(primes, L)
r_num = bisect_right(primes, R)
print(r_num - l_num)
