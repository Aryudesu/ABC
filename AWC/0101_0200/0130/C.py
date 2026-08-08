MOD = 10 ** 9 + 7
N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = [0] * K
dp[0] = 1
for a in A:
    newDP = dp.copy()
    for k in range(K):
        newDP[(a + k) % K] += dp[k]
        newDP[(a + k) % K] %= MOD
    dp = newDP
print((dp[0] - 1) % MOD)
