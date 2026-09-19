N, M, K = map(int, input().split())
H = list(map(int, input().split()))
meshi = [0] * N
for _ in range(M):
    p, r = map(int, input().split())
    meshi[p-1] = r
INF = 10 ** 18
dp = [-INF] * N
dp[0] = K
isOk = True
for idx in range(N):
    nowHP = dp[idx] - H[idx]
    if nowHP < 0:
        nowHP = -10**18
    else:
        nowHP += meshi[idx]
    if idx + 1 < N:
        dp[idx+1] = max(dp[idx+1], nowHP)
    if idx + 2 < N:
        dp[idx+2] = max(dp[idx+2], nowHP)
res = dp[-1] - H[-1]
if res < 0:
    print(-1)
else:
    print(res + meshi[-1])
