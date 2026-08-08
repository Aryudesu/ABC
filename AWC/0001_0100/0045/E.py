from atcoder.segtree import SegTree
from atcoder.fenwicktree import FenwickTree

INF = 10 ** 18
N, W, K = map(int, input().split())
A = list(map(int, input().split()))
ft = FenwickTree(N)
st = SegTree(min, INF, A)
for i in range(N):
    ft.add(i, A[i])
result = -INF
for l in range(N - W + 1):
    value1 = ft.sum(l, l + W)
    value2 = st.prod(l, l + W) * K
    result = max(result, value1 + value2)
    # print(l, l + W, value1, value2)
print(result)
