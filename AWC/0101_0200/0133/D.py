from collections import defaultdict

N, T = map(int, input().split())
dp = [0] * (T + 5)
LRV = defaultdict(list)
for n in range(N):
    l, r, v = map(int, input().split())
    LRV[l].append((r, v))
for t in range(T+1):
    value = dp[t]
    # print(dp)
    dp[t + 1] = max(dp[t + 1], dp[t])
    if t in LRV:
        for r, v in LRV[t]:
            dp[r + 1] = max(dp[r + 1], dp[t] + v)
# print(dp)
print(dp[T+1])
