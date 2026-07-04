from sortedcontainers import SortedSet
from collections import defaultdict
H, W, Q = map(int, input().split())

HData = defaultdict(SortedSet)
WData = defaultdict(SortedSet)
verticalNums = set()
for q in range(Q+1):
    verticalNums.add(q)
colorData = ["A"]
result = [[-1] * W for _ in range(H)]
result[-1][-1] = 0
for q in range(Q):
    r, c, x = input().split()
    r, c = int(r), int(c)
    colorData.append(x)
    result[r-1][c-1] = q + 1
for h in range(H-1, -1, -1):
    tmp = -1
    for w in range(W-1, -1, -1):
        tmp = max(tmp, result[h][w])
        result[h][w] = tmp
for w in range(W-1, -1, -1):
    tmp = -1
    for h in range(H-1, -1, -1):
        tmp = max(tmp, result[h][w])
        result[h][w] = tmp
for h in range(H):
    tmp = []
    for w in range(W):
        tmp.append(colorData[result[h][w]])
    print("".join(tmp))

