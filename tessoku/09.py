H, W, N = [int(l) for l in input().split()]
field = [[0] * W for _ in range(H)]
for n in range(N):
    a, b, c, d = map(int, input().split())
    a, b, c, d = a-1, b-1, c-1, d-1
    field[a][b] += 1
    if d + 1 < W:
        field[a][d + 1] -= 1
    if c + 1 < H:
        field[c+1][b] -= 1
        if d + 1 < W:
            field[c+1][d+1] += 1
for h in range(H):
    s = 0
    for w in range(W):
        s += field[h][w]
        field[h][w] = s

for w in range(W):
    s = 0
    for h in range(H):
        s += field[h][w]
        field[h][w] = s
for f in field:
    print(*f)
