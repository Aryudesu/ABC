N, M, K = map(int, input().split())
W = []
V = []
dp = [[0] * (K + 1) for _ in range(N + 1)] 
for n in range(N):
    c, t, p = map(int, input().split())
    W.append(t)
    V.append(p-c)
for i in range(N):
    for j in range(K + 1):
        if j < W[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - W[i]] + V[i])
print(dp[N][K] * M)
