from collections import defaultdict

INF = 10**18
N = int(input())
XY = []
for n in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))
dist = [[0] * N for _ in range(N)]
for n in range(N):
    for m in range(N):
        dist[n][m] = (XY[n][0] - XY[m][0]) ** 2 + (XY[n][1] - XY[m][1]) ** 2

dp = defaultdict(lambda: INF)
# 開始地点だから0
dp[(1 << 0, 0)] = 0
for _ in range(N-1):
    nextDP = defaultdict(lambda: INF)
    for mask, pos in dp:
        for nextPos in range(N):
            if mask & (1 << nextPos):
                continue
            nowDist = dp[(mask, pos)]
            nextDist = nowDist + dist[pos][nextPos]
            nextMask = mask | (1 << nextPos)
            nextDP[(nextMask, nextPos)] = min(nextDP[(nextMask, nextPos)], nextDist)
    dp = nextDP
# print(dp)
result = INF
for mask, pos in dp:
    nowDist = dp[(mask, pos)]
    result = min(result, nowDist + dist[pos][0])
print(result)
