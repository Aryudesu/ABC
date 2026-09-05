H, W, K = map(int, input().split())
S = [input() for _ in range(H)]
# 可能個数
field = [[False] * W for _ in range(H)]
result = set()
nodes = set()
safeH = set()
safeW = set()
for h in range(H):
    f = True
    for w in range(W):
        if S[h][w] == "#":
            f = False
            break
    if f:
        safeH.add(h)

for w in range(W):
    f = True
    for h in range(H):
        if S[h][w] == "#":
            f = False
            break
    if f:
        for h in safeH:
            field[h][w] = True
            nodes.add((h, w))
            result.add((h, w))

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(K):
    nextNodes = set()
    for h, w in nodes:
        for dh, dw in dirs:
            nh, nw = h + dh, w + dw
            if not (0 <= nh < H):
                continue
            if not (0 <= nw < W):
                continue
            if S[nh][nw] == "#":
                continue
            if field[nh][nw]:
                continue
            nextNodes.add((nh, nw))
            result.add((nh, nw))
            field[nh][nw] = True
    nodes = nextNodes
print(len(result))
