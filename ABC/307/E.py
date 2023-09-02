def calc(N, M):
    MOD = 998244353
    C = M - 1
    O = 0
    for n in range(N - 2):
        tmpC = (C * (M - 1)) % MOD
        tmpO = (C - O) % MOD
        C = tmpC
        O = tmpO
    return ((C - O) * M) % MOD


N, M = [int(l) for l in input().split()]
print(calc(N, M))
