def inv_mod(num, MOD):
    return pow(num, MOD-2, MOD)


MOD = 998244353
N, X = [int(l) for l in input().split()]
T = [int(l) for l in input().split()]
Dat = [0] * (X + 1)
Dat[0] = 1
bunbo = 0
bunshi = 0
for i in range(X + 1):
    f = False
    for idx in range(N):
        n_idx = i + T[idx]
        if n_idx > X:
            if idx == 0:
                bunshi = (bunshi * N + Dat[i]) % MOD
            if not f:
                bunbo = (bunbo * N) % MOD
                f = True
            continue
        Dat[n_idx] += Dat[i]
    print(Dat, bunshi, bunbo)
print(bunshi, bunbo)
print((inv_mod(bunbo, MOD) * bunshi) % MOD)
