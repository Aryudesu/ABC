H, W = map(int, input().split())
INF = H * W + 10 + (H * W) % 2
S = [input() for _ in range(H)]
blackField = [[INF] * W for _ in range(H)]
whiteField = [[INF] * W for _ in range(H)]
blackNodes = set()
whiteNodes = set()
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            blackNodes.add((h, w))
            blackField[h][w] = 0
        else:
            whiteNodes.add((h, w))
            whiteField[h][w] = 0

if len(blackNodes) == 0 or len(whiteNodes) == 0:
    for h in range(H):
        res = []
        for w in range(W):
            res.append(".")
        print("".join(res))
    exit(0)

dirs = []
for dh in range(-1, 2):
    for dw in range(-1, 2):
        if dh != 0 or dw != 0:
            dirs.append((dh, dw))

c = 0
while blackNodes:
    newNodes = set()
    c += 1
    for h, w in blackNodes:
        for dh, dw in dirs:
            if not (0 <= h + dh < H):
                continue
            if not (0 <= w + dw < W):
                continue
            nh, nw = h + dh, w + dw
            if blackField[nh][nw] <= c:
                continue
            blackField[nh][nw] = c
            newNodes.add((nh, nw))
    blackNodes = newNodes

c = 0
while whiteNodes:
    newNodes = set()
    c += 1
    for h, w in whiteNodes:
        for dh, dw in dirs:
            if not (0 <= h + dh < H):
                continue
            if not (0 <= w + dw < W):
                continue
            nh, nw = h + dh, w + dw
            if whiteField[nh][nw] <= c:
                continue
            whiteField[nh][nw] = c
            newNodes.add((nh, nw))
    whiteNodes = newNodes

for h in range(H):
    res = []
    fb = blackField[h]
    fw = whiteField[h]
    for w in range(W):
        if fb[w] == 0 and fw[w] % 2 == 0:
            res.append(".")
        elif fw[w] == 0 and fb[w] % 2 == 0:
            res.append("#")
        else:
            res.append(S[h][w])
    print("".join(res))
