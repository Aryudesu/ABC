def calc(N):
    if N == 1:
        return 4
    if N == 2:
        return 16 - 1
    MOD = 998244353
    k = 2
    for _ in range(N):
        k = (k * k) % MOD
    l = 8
    s = 0
    for _ in range(2, N-1):
        c = 2 ** _
        s += ((2 ** (l - 2)) * c * (c - 1))
        s %= MOD
    return (k - s) % MOD

N = int(input())
print(calc(N))
