import math

from atcoder.dsu import DSU
from atcoder.math import inv_mod


def calcXYtoNum(x, y, w):
    return y * w + x

# 呼び出し
MOD = 998244353
H, W = [int(l) for l in input().split()]
N = H * W
S = []
for h in range(H):
    S.append(input())
uf = DSU(H * W)
for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            continue
        n1 = calcXYtoNum(w, h, W)
        if w > 0:
            if S[h][w - 1] == "#":
                n2 = calcXYtoNum(w - 1, h, W)
                uf.merge(n1, n2)
        if w + 1 < W:
            if S[h][w + 1] == "#":
                n2 = calcXYtoNum(w + 1, h, W)
                uf.merge(n1, n2)
        if h > 0:
            if S[h - 1][w] == "#":
                n2 = calcXYtoNum(w, h - 1, W)
                uf.merge(n1, n2)
        if h + 1 < H:
            if S[h + 1][w] == "#":
                n2 = calcXYtoNum(w, h + 1, W)
                uf.merge(n1, n2)

greenIslands = set()
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            n1 = calcXYtoNum(w, h, W)
            tmp = uf.leader(n1)
            greenIslands.add(tmp)
GNum = len(greenIslands)
denom = 0
mole = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue
        denom += 1
        islandPatterns = set()
        n1 = calcXYtoNum(w, h, W)
        if w > 0:
            if S[h][w - 1] == "#":
                n2 = calcXYtoNum(w - 1, h, W)
                islandPatterns.add(uf.leader(n2))
        if w + 1 < W:
            if S[h][w + 1] == "#":
                n2 = calcXYtoNum(w + 1, h, W)
                islandPatterns.add(uf.leader(n2))
        if h > 0:
            if S[h - 1][w] == "#":
                n2 = calcXYtoNum(w, h - 1, W)
                islandPatterns.add(uf.leader(n2))
        if h + 1 < H:
            if S[h + 1][w] == "#":
                n2 = calcXYtoNum(w, h + 1, W)
                islandPatterns.add(uf.leader(n2))
        mole += GNum - len(islandPatterns) + 1
g = math.gcd(mole, denom)
mole = mole//g
denom = denom//g
print((mole * inv_mod(denom, MOD)) % MOD)
