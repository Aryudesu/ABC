from typing import Tuple
INF = 160005
def calcDist(H: int, W: int, S: list[str], start: Tuple[int, int])->dict[Tuple[int, int], int]:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    field = [[INF] * W for _ in range(H)]
    result = {start: 0}
    node = set()
    node.add(start)
    field[start[0]][start[1]] = 0
    while node:
        nextNode = set()
        for h, w in node:
            if S[h][w] == "#":
                continue
            nowDist = field[h][w]
            for dh, dw in dirs:
                nh, nw = h + dh, w + dw
                if not (0 <= nh < H):
                    continue
                if not (0 <= nw < W):
                    continue
                if S[nh][nw] == "#":
                    continue
                nextDist = nowDist + 1
                if field[nh][nw] <= nextDist:
                    continue
                field[nh][nw] = nextDist
                nextNode.add((nh, nw))
                if S[nh][nw] == "F":
                    result[(nh, nw)] = nextDist
        node = nextNode
    return result
        

H, W, K = map(int, input().split())
S = [input() for _ in range(H)]
start = None
goal = None
cats = []
for h in range(H):
    for w in range(W):
        if S[h][w] == "@":
            start = (h, w)
        elif S[h][w] == "G":
            goal = (h, w)
        elif S[h][w] == "F":
            cats.append((h, w))
s2c = calcDist(H, W, S, start)
g2c = calcDist(H, W, S, goal)
# print(s2c)
# print(g2c)
if len(s2c) < K + 1 or len(g2c) < K + 1:
    print(-1)
    exit(0)

s2cDist = []
g2cDist = []
for k in range(K):
    s2cDist.append(s2c[cats[k]])
    g2cDist.append(g2c[cats[k]])
c2cDist = [[0] * K for _ in range(K)]

for k1 in range(K):
    c2c = calcDist(H, W, S, cats[k1])
    # print(c2c)
    for k2 in range(K):
        c2cDist[k1][k2] = c2c[cats[k2]]

allcats = (1 << K) - 1
data = [[INF] * K for _ in range(1 << K)]
for k in range(K):
    b = 1 << k
    data[b][k] = s2cDist[k]
# print(data)
for mask in range(1, 1 << K):
    for nowPos in range(K):
        if data[mask][nowPos] >= INF:
            continue
        nowDist = data[mask][nowPos]
        remain = allcats ^ mask
        while remain:
            nextPos = remain.bit_length() - 1
            b = 1 << nextPos
            remain = remain ^ b
            nextMask = mask | b
            nextDist = nowDist + c2cDist[nowPos][nextPos]
            data[nextMask][nextPos] = min(data[nextMask][nextPos], nextDist)
result = INF
for k in range(K):
    d = data[-1][k] + g2cDist[k]
    result = min(result, d)
print(result)
