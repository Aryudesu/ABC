N, W = map(int, input().split())
# その重さの最大価値
dp = [0] * (W + 1)
for n in range(N):
    w, v = map(int, input().split())
    for nowW in range(W, -1, -1):
        if nowW + w > W:
            continue
        nowV = dp[nowW]
        dp[nowW + w] = max(dp[nowW + w], nowV + v)
print(max(dp))
