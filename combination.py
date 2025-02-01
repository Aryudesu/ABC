N = 24
dp = [1]
for n in range(N):
    print(dp)
    M = n + 2
    new_dp = [0] * M
    for m in range(M - 1):
        new_dp[m] += dp[m]
    for m in range(M - 1):
        new_dp[m + 1] += dp[m]
    dp = new_dp
print(dp)
