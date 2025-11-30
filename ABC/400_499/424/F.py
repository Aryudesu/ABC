import sys
from atcoder.segtree import SegTree

def op(x, y):
    sx, mx = x
    sy, my = y
    return (sx + sy, min(mx, sx + my))

input = sys.stdin.readline
N, Q = map(int, input().split())
seg = SegTree(op, (0, 0), [(0, 0)] * (N + 1))

ans = []
for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    s, mn = seg.prod(a, b + 1)
    if s == 0 and mn >= 0:
        seg.set(a, (1, 0))
        seg.set(b, (-1, -1))
        print("Yes")
    else:
        print("No")
