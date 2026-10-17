from atcoder.segtree import SegTree

N, Q = map(int, input().split())
L = [0] + list(map(int, input().split()))
R = list(map(int, input().split())) + [0]
lst = SegTree(min, 10**18, L)
rst = SegTree(min, 10**18, R)
result = []
for _ in range(Q):
    s, t = map(int, input().split())
    if s == t:
        result.append(0)
    if s < t:
        result.append(min(R[s-1], rst.prod(0, s) + L[s-1]))
    else:
        result.append(min(L[s-1], lst.prod(s, N) + R[s-1]))
print(*result, sep="\n")
