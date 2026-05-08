N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
MOD = 10**9 + 7
dp = [0] * (K + 3)
dp[0] = 1
for a in A:
    nextDP = [0] * (K + 3)
    s = 0
    for r in range(K+3):
        s += dp[r]
        l = r - a - 1
        if l >= 0:
            s -= dp[l]
        nextDP[r] += s
        nextDP[r] %= MOD
    dp = nextDP
print(dp[K]%MOD)
