from atcoder.fenwicktree import FenwickTree

H, W, Q = map(int, input().split())
minFt = FenwickTree(H)
maxFt = FenwickTree(H)
for h in range(H):
    l, r = map(int, input().split())
    minFt.add(h, l-1)
    maxFt.add(h, r-1)

