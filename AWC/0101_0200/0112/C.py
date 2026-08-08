MOD = 10**9 + 7
N, K = map(int, input().split())
P = list(map(int, input().split()))
dp = [0] * (K + 1)
dp[0] = 1
for p in P:
    for k in range(K, -1, -1):
        if p + k > K:
            continue
        dp[k + p] += dp[k]
        dp[k + p] %= MOD
print(dp[-1])
