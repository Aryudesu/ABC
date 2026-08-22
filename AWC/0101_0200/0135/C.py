N, M = map(int, input().split())
field = []
for n in range(N):
    field.append(list(map(int, input().split())))
dp = [[0] * M for _ in range(N)]
dp[0][0] = field[0][0]
H, W = N, M
for h in range(H):
    for w in range(W):
        if h + 1 < H:
            dp[h + 1][w] = max(dp[h + 1][w], dp[h][w] + field[h + 1][w])
        if w + 1 < W:
            dp[h][w + 1] = max(dp[h][w + 1], dp[h][w] + field[h][w + 1])
print(dp[-1][-1])
