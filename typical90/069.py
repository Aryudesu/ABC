def calc(N, K):
    MOD = (10 ** 9) + 7
    tmp = K % MOD
    if N == 1:
        return tmp
    tmp = (tmp * (K - 1)) % MOD
    if N == 2:
        return tmp
    tmp = (tmp * pow(K - 2, N - 2, MOD)) % MOD
    return tmp

N, K = [int(l) for l in input().split()]
print(calc(N, K))
