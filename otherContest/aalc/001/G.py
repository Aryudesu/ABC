from atcoder.lazysegtree import LazySegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(Q):
    n, a, b, c = map(int, input().split())
