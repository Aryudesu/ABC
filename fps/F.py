N = int(input())
MOD = 998244353
print(((pow(3, N, MOD) - pow(-1, N, MOD)) * pow(4, MOD-2, MOD)) % MOD)