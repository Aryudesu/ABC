from collections import defaultdict
from sortedcontainers import SortedSet

H, W, Q = map(int, input().split())
S = [input() for _ in range(H)]
hData = defaultdict(SortedSet)
wData = defaultdict(SortedSet)
buildData = set()
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
s = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == "B":
            rf = False
            for dh, dw in dirs:
                if not (0 <= h + dh < H):
                    continue
                if not (0 <= w + dw < W):
                    continue
                nh, nw = h + dh, w + dw
                if S[nh][nw] == "R":
                    rf = True
                    break
            if rf:
                s += 1
            else:
                hData[h].add(w)
                wData[w].add(h)
# print(hData)
# print(wData)
for _ in range(Q):
    u, d, l, r = map(int, input().split())
    u-=1
    d-=1
    l-=1
    r-=1
    if u - 1 >= 0:
        lidx = hData[u-1].bisect_left(l)
        ridx = hData[u-1].bisect_right(r)
        for idx in range(ridx-1, lidx-1, -1):
            t = hData[u-1][idx]
            hData[u-1].discard(t)
            wData[t].discard(u-1)
            s += 1
    if d + 1 < H:
        lidx = hData[d+1].bisect_left(l)
        ridx = hData[d+1].bisect_right(r)
        for idx in range(ridx-1, lidx-1, -1):
            t = hData[d+1][idx]
            hData[d+1].discard(t)
            wData[t].discard(d+1)
            s += 1
    if l - 1 >= 0:
        lidx = wData[l-1].bisect_left(u)
        ridx = wData[l-1].bisect_right(d)
        for idx in range(ridx-1, lidx-1, -1):
            t = wData[l-1][idx]
            wData[l-1].discard(t)
            hData[t].discard(l-1)
            s += 1
    if r + 1 < H:
        lidx = wData[r+1].bisect_left(u)
        ridx = wData[r+1].bisect_right(d)
        for idx in range(ridx-1, lidx-1, -1):
            t = wData[r+1][idx]
            wData[r+1].discard(t)
            hData[t].discard(r+1)
            s += 1
    # print(hData)
    # print(wData)
    print(s)
