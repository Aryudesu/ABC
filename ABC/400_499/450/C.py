def bfs(H, W, S, field, sth, stw):
    if S[sth][stw] == "#":
        return False
    node = {(sth, stw)}
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    isOk = True
    while node:
        nextNode = set()
        for h, w in node:
            for dh, dw in dir:
                if not (0 <= dh + h < H and 0 <= dw + w < W):
                    isOk = False
                    continue
                newH, newW = dh + h, dw + w
                if S[newH][newW] == "#":
                    continue
                if field[newH][newW]:
                    continue
                field[newH][newW] = True
                nextNode.add((newH, newW))
        node = nextNode
    return isOk


H, W = map(int, input().split())
S = []
for h in range(H):
    S.append(input())
field = [[False] * W for _ in range(H)]
result = 0
for h in range(H):
    for w in range(W):
        if field[h][w]:
            continue
        res = bfs(H, W, S, field, h, w)
        if res:
            result += 1
print(result)
