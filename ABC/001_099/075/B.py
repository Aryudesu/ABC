H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue
        count = 0
        for dh in range(-1, 2):
            for dw in range(-1, 2):
                nh, nw = h + dh, w + dw
                if not (0 <= nh < H and 0 <= nw < W):
                    continue
                if S[nh][nw] == "#":
                    count += 1
        S[h][w] = str(count)
for h in range(H):
    print("".join(S[h]))

