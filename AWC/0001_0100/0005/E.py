from atcoder.segtree import SegTree

INF = 10 ** 10

N, Q = map(int, input().split())
A = list(map(int, input().split()))
lst = SegTree(max, -INF, A)

result = []
for q in range(Q):
    l, r = map(int, input().split())
    result.append(lst.prod(l-1, r))
for r in result:
    print(r)
