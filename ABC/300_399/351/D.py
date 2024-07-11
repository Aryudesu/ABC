from atcoder.dsu import DSU

H, W = [int(l) for l in input().split()]
dsu = DSU(H * W)
S = []
field = [[False] * W for h in range(H)]
for h in range(H):
    S.append(input())

for h in range(H):
    for w in range(W):
        tmp = True
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i * j != 0:
                    continue
                if h + i >= 0 and h + i < H and w + j >= 0 and w + j < W:
                    if S[h + i][w + j] == "#":
                        tmp = False
                        break
            if not tmp:
                break
        if tmp:
            field[h][w] = True
for h in range(H):
    for w in range(W):
        n = h * W + w
        if not field[h][w]:
            continue
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i * j != 0:
                    continue
                if h + i >= 0 and h + i < H and w + j >= 0 and w + j < W:
                    if field[h + i][w + j]:
                        m = (h + i) * W + (w + j)
                        dsu.merge(n, m)
groups = dsu.groups()
data = []
for group in groups:
    data.append(set(group))
result = 0
for dat in data:
    newDat = set()
    for p in dat:
        newDat.add(p)
        h, w = p // W, p % W
        # print(h, w)
        if not field[h][w]:
            continue
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i * j != 0:
                    continue
                if h + i >= 0 and h + i < H and w + j >= 0 and w + j < W:
                    m = (h + i) * W + (w + j)
                    newDat.add(m)
    # print(newDat)
    if result < len(newDat):
        result = len(newDat)
print(result)
