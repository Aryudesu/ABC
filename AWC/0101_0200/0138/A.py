H, W = map(int, input().split())
S = [input() for _ in range(H)]
u, l, d, r = H, W, 0, 0
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            u = min(u, h)
            l = min(l, w)
            d = max(d, h)
            r = max(r, w)
print((r - l + 1) * (d - u + 1))
