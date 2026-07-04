N, X = map(int, input().split())
A = list(map(int, input().split()))
dp = dict()
dp[0] = 1
bunshi = 0
bunbo = 0
MOD = 998244353
for a in A:
    newDP = dp.copy()
    for key, value in dp.items():
        if key + a >= X:
            bunshi = (bunshi + (key + a) * value) % MOD
            bunbo = (bunbo + value) % MOD
        else:
            newDP[key + a] = newDP.get(key + a, 0) + value
    dp = newDP
print((bunshi * pow(bunbo, MOD-2, MOD)) % MOD)
