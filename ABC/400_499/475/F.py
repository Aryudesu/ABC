H, W = map(int, input().split())
field = [[0] * W for _ in range(H)]
S = [input() for _ in range(H)]
all = (H * (H-1) * W * (W - 1)) // 4
res = 0
for h in range(H):
    tmp = 0
    for w in range(W):
        if S[h][w] == "#":
            tmp += 1
        else:
            res += (tmp * (tmp + 1)) * (H - 1)
            tmp = 0
    res += (tmp * (tmp + 1)) * (H - 1)
for w in range(W):
    tmp = 0
    for h in range(H):
        if S[h][w] == "#":
            tmp += 1
        else:
            res += (tmp * (tmp + 1)) * (W - 1)
            tmp = 0
    res += (tmp * (tmp + 1)) * (W - 1)
print(all - res)            
