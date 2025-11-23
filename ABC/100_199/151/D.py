def calcDepth(H, W, sy, sx, S):
    memo = [[H * W + 10] * W for _ in range(H)]
    memo[sy][sx] = 0
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 0
    nodes = set()
    nodes.add((sy, sx))
    while nodes:
        count += 1
        nextNodes = set()
        for y, x in nodes:
            for dy, dx in dirs:
                ny = y + dy
                nx = x + dx
                if not (0 <= ny < H and 0 <= nx < W):
                    continue
                if S[ny][nx] == "#":
                    continue
                if memo[ny][nx] <= count:
                    continue
                nextNodes.add((ny, nx))
                memo[ny][nx] = count
        nodes = nextNodes
    # 最後何もなくなった場合は進めなくなったということなので1を引く
    return count - 1

H, W = map(int, input().split())
S = [input() for h in range(H)]
result = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue
        result = max(result, calcDepth(H, W, h, w, S))
print(result)
