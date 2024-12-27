N = int(input())
MOD = 10 ** 9 + 7
res1 = pow(4, N + 1, MOD) - 1
res2 = (4 - 1)
print((res1 * pow(res2, MOD-2, MOD)) % MOD)
