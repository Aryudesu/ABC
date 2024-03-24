def fact(N):
    res = 1
    for n in range(1, N + 1):
        res = (res * n) % 998244353
    return res


def combination(N, M):
    if M*2 > N:
        M = N - M
    res = 1
    for m in range(M):
        res *= (N - m)
    for m in range(1, M + 1):
        res //= m
    return res


N = int(input())
result = fact(N ** 2) % 998244353
res = N ** 2 % 998244353
res = (res * (combination(N ** 2, 2 * N - 1) % 998244353) ) % 998244353
res = (res * fact(N - 1)) % 998244353
res = (res * fact(N - 1)) % 998244353
res = (res * fact((N - 1) ** 2)) % 998244353
print((result - res) % 998244353)
