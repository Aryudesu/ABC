def calc(H, W, S):
    umin = H
    lmin = W
    dmax = 0
    rmax = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                if umin > h:
                    umin = h
                if lmin > w:
                    lmin = w
                if dmax < h:
                    dmax = h
                if rmax < w:
                    rmax = w
    for h in range(dmax - umin + 1):
        for w in range(rmax - lmin + 1):
            if S[umin + h][lmin + w] != "#":
                print(umin + h + 1, lmin + w + 1)
                return
    raise Exception()


H, W = [int(l) for l in input().split()]
S = [input() for _ in range(H)]
calc(H, W, S)
