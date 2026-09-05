H, W = map(int, input().split())
S = [input() for _ in range(H)]
l, u, r, d = W, H, 0, 0
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            l = min(l, w)
            u = min(u, h)
            r = max(r, w)
            d = max(d, h)
print(max(0, ((r - l + 1) + (d - u + 1)) * 2))
