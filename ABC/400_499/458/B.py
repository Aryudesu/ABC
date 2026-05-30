H, W = map(int, input().split())
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for h in range(H):
    res = []
    for w in range(W):
        c = 0
        for dh, dw in dir:
            if 0 <= h + dh < H and 0 <= w + dw < W:
                c += 1
        res.append(c)
    print(*res)
        
