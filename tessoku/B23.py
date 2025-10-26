import math

N = int(input())
pts = [tuple(map(int, input().split())) for _ in range(N)]

# 距離前計算
dist = [[0.0]*N for _ in range(N)]
for i in range(N):
    xi, yi = pts[i]
    for j in range(N):
        xj, yj = pts[j]
        dist[i][j] = math.hypot(xi - xj, yi - yj)

INF = 10**18
M = 1 << N
dp = [[INF]*N for _ in range(M)]
dp[1 << 0][0] = 0.0

for mask in range(M):
    for i in range(N):
        if dp[mask][i] == INF:
            continue
        for j in range(N):
            if mask & (1 << j):
                continue
            nxt = mask | (1 << j)
            nd = dp[mask][i] + dist[i][j]
            if nd < dp[nxt][j]:
                dp[nxt][j] = nd

full = M - 1
ans = INF
for i in range(N):
    tour_cost = dp[full][i] + dist[i][0]
    if tour_cost < ans:
        ans = tour_cost

print(ans)
