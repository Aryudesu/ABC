from collections import defaultdict

H, W = 2000, 2000
sky = [[0 for _ in range(W)] for _ in range(H)]
sky2 = [[0 for _ in range(W)] for _ in range(H)]
N = int(input())
for n in range(N):
    m = n + 1
    u, d, l, r = map(int, input().split())
    u, l = u-1, l-1
    sky[u][l] += 1
    sky2[u][l] += m
    if r < W:
        sky[u][r] += -1
        sky2[u][r] += -m
    if d < H:
        sky[d][l] += -1
        sky2[d][l] += -m
    if d < H and r < W:
        sky[d][r] += 1
        sky2[d][r] += m
for h in range(H):
    tmp = 0
    tmp2 = 0
    for w in range(W):
        tmp += sky[h][w]
        tmp2 += sky2[h][w]
        sky[h][w] = tmp
        sky2[h][w] = tmp2

for w in range(W):
    tmp = 0
    tmp2 = 0
    for h in range(H):
        tmp += sky[h][w]
        tmp2 += sky2[h][w]
        sky[h][w] = tmp
        sky2[h][w] = tmp2
data = defaultdict(int)
allc = 0
for h in range(H):
    for w in range(W):
        if sky[h][w] == 1:
            data[sky2[h][w]] += 1
        if sky[h][w] != 0:
            allc += 1
for i in range(N):
    print(H * W  - allc + data[i+1])
