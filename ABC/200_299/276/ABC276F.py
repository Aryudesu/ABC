def inverseMod(num, MOD):
    return pow(num, MOD-2, MOD)


N = int(input())
A = [int(l) for l in input().split()]
A.sort()
MOD = 998244353
bunshi = 0
bunbo = N * N
for idx in range(N):
    bunshi = (bunshi + idx * A[idx]) % MOD
    print((bunshi * inverseMod(bunbo, MOD)) % MOD)
