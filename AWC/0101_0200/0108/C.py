from atcoder.segtree import SegTree
from atcoder.fenwicktree import FenwickTree

INF = 10 ** 18
N, K = map(int, input().split())
F = list(map(int, input().split()))
st = SegTree(max, -INF, F)
ft = FenwickTree(N)
for i in range(N):
    ft.add(i, F[i])
res = INF
for i in range(N - K + 1):
    s1 = ft.sum(i, i + K)
    l = st.prod(0, i)
    r = st.prod(i+K, N)

    tmp = -INF
    tmp = max(tmp, s1)
    if i > 0:
        tmp = max(tmp, l * K)
    if i < N - K:
        tmp = max(tmp, r * K)
    res = min(res, tmp)
print(res/K)
