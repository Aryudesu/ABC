A, B, C, D, E, F = [int(l) for l in input().split()]
MOD = 998244353
L = (A * B * C) % MOD
R = (D * E * F) % MOD
print((L - R) % MOD)
