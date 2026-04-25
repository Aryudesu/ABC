N, S = map(int, input().split())
dp = [0] * (S + 1)
for n in range(N):
    v, c = map(int, input().split())
    for s in range(S, -1, -1):
        if s + c > S:
            continue
        if dp[s] == 0 and s > 0:
            continue
        dp[s + c] = max(dp[s + c], dp[s] + v)
if dp[-1] > 0:
    print(dp[-1])
else:
    print(-1)
