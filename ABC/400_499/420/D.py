from collections import defaultdict
from heapq import heappop, heappush

INF = 10**18


H, W = [int(l) for l in input().split()]
# 0 偶数回押した 1奇数回押した
field = []
for h in range(H):
    field.append(input())
distData = defaultdict(lambda:INF)
start = None
goal1 = None
goal2 = None
for h in range(H):
    for w in range(W):
        if field[h][w] == "S":
            start = (0, h, w)
        if field[h][w] == "G":
            goal1 = (0, h, w)
            goal2 = (1, h, w)
distData[start] = 0
Q = []
heappush(Q, (distData[start], start))
while Q:
    # 優先度（距離）が最小であるキューを取り出す
    dist_u, u = heappop(Q)
    if distData[u] < dist_u:
        continue
    n, h, w = u
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 and j != 0:
                continue
            if i == 0 and j == 0:
                continue
            if h + i < 0 or h + i >= H:
                continue
            if w + j < 0 or w + j >= W:
                continue
            if field[h + i][w + j] == "#":
                continue
            v = (n, h + i, w + j)
            v2 = (1-n, h + i, w + j)
            alt = dist_u + 1
            if field[h + i][w + j] == "." or field[h + i][w + j] == "S" or field[h + i][w + j] == "G":
                if distData[v] > alt:
                    distData[v] = alt
                    heappush(Q, (alt, v))
            if field[h + i][w + j] == "?":
                if distData[v2] > alt:
                    distData[v2] = alt
                    heappush(Q, (alt, v2))
            if field[h + i][w + j] == "o" and n == 0:
                if distData[v] > alt:
                    distData[v] = alt
                    heappush(Q, (alt, v))
            if field[h + i][w + j] == "x" and n == 1:
                if distData[v] > alt:
                    distData[v] = alt
                    heappush(Q, (alt, v))
res = min(distData[goal1], distData[goal2])
print(res if res < INF else -1)
