from atcoder.fenwicktree import FenwickTree
from atcoder.segtree import SegTree

INF = 10 ** 18
N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))
WM = max(W)
ft = FenwickTree(N)
st = SegTree(max, -INF, N)
for n in range(N):
    ft.add(n, H[n])
    st.set(n, H[n])
S = sum(H)
result = S
for i in range(N):
    mx = st.prod(i, min(N, i + WM))
    sm = ft.sum(i, min(N, i + WM))
    res = S - sm + mx * (min(N, i + WM) - i)
    result = max(res, result)
print(result)
