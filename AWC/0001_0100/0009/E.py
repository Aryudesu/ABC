from atcoder.segtree import SegTree
INF = 10 ** 10
N, Q = map(int, input().split())
A = list(map(int, input().split()))
maxSt = SegTree(max, -INF, A)
minSt = SegTree(min, INF, A)
result = []
for q in range(Q):
    l, r = map(int, input().split())
    result.append(maxSt.prod(l-1, r) - minSt.prod(l-1, r))
for r in result:
    print(r)

