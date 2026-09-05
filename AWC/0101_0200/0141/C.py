H, W = map(int, input().split())
G = []
for h in range(H):
    G.append(list(map(int, input().split())))
field = [[[0, 0, 0] for _ in range(W)] for _ in range(H)]
for w in range(W):
    field[0][w][1] = G[0][w]
for h in range(H-1):
    for w in range(W):
        for d1 in range(3):
            psc = field[h][w][d1]
            for d2 in range(3):
                if d1 - 1 and d1 == d2:
                    continue
                if not (0 <= w + d2 - 1 < W):
                    continue
                field[h+1][w+d2-1][d2] = max(field[h+1][w+d2-1][d2], field[h][w][d1] + G[h+1][w+d2-1])
result = 0
for w in range(W):
    result = max(result, max(field[-1][w]))
print(result)
