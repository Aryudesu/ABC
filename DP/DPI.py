N = int(input())
P = [float(l) for l in input().split()]
dp = {0: 1}
for n in range(N):
    new_dp = dict()
    for k in dp:
        new_dp[k] = new_dp.get(k, 0) + dp[k] * (1 - P[n])
        new_dp[k + 1] = new_dp.get(k + 1, 0) + dp[k] * P[n]
    dp = new_dp
result = 0
for n in range(N//2 + 1, N + 1):
    result += dp[n]
print(result)
