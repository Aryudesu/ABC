from collections import defaultdict

N = int(input())
dist = [[0] * N for _ in range(N)]
XYZ = []
for _ in range(N):
    x, y, z = map(int, input().split())
    XYZ.append((x, y, z))
# dist[n][m]はnからmに遷移
for n in range(N):
    for m in range(N):
        dist[n][m] = abs(XYZ[m][0] - XYZ[n][0]) + abs(XYZ[m][1] - XYZ[n][1]) + max(0, XYZ[m][2] - XYZ[n][2])
FULL = (1 << N) - 1
INF = 10 ** 18
dp = defaultdict(lambda: INF)
for i in range(N):
    dp[(1, 0)] = 0

for _ in range(N-1):
    nextDP = defaultdict(lambda: INF)
    for key in dp:
        # print(key)
        mask, frm = key
        for i in range(N):
            bit = 1<<i
            if bit & mask != 0:
                continue
            nextDP[(bit|mask, i)] = min(nextDP[(bit|mask, i)], dp[key] + dist[frm][i])
    dp = nextDP
result = INF
for key in dp:
    mask, frm = key
    result = min(result, dp[key] + dist[frm][0])
print(result)
