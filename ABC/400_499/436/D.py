from collections import defaultdict

H, W = map(int, input().split())
S = [input() for _ in range(H)]

INF = H * W + 5
field = [[INF] * W for _ in range(H)]
field[0][0] = 0
warpMap = dict()
for h in range(H):
    for w in range(W):
        if S[h][w] == "." or S[h][w] == "#":
            continue
        tmp = warpMap.get(S[h][w], [])
        tmp.append((h, w))
        warpMap[S[h][w]] = tmp


dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
nodes = {(0, 0)}
goalF = False
warpEnd = set()
while nodes:
    new_nodes = set()
    for h, w in nodes:
        now_count = field[h][w]
        for dh, dw in dirs:
            if not (0 <= h + dh < H and 0 <= w + dw < W):
                continue
            if field[h+dh][w+dw] <= now_count + 1:
                continue
            if S[h+dh][w+dw] == "#":
                continue
            field[h+dh][w+dw] = now_count + 1
            new_nodes.add((h+dh, w+dw))
            if h+dh == H-1 and w+dw == W-1:
                goalF = True
                break
        if S[h][w] != "." and S[h][w] != "#":
            if S[h][w] in warpEnd:
                continue
            for nh, nw in warpMap.get(S[h][w], []):
                warpEnd.add(S[h][w])
                if field[nh][nw] <= now_count + 1:
                    continue
                field[nh][nw] = now_count + 1
                new_nodes.add((nh, nw))
                if nh == H-1 and nw == W-1:
                    goalF = True
                    break
    if goalF:
        break
    nodes = new_nodes
res = field[-1][-1]
if res == INF:
    print(-1)
else:
    print(field[-1][-1])
