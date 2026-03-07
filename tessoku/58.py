from atcoder.segtree import SegTree

N, Q = map(int, input().split())
st = SegTree(max, 0, N+1)
for _ in range(Q):
    n, a, b = map(int, input().split())
    if n == 1:
        st.set(a-1, b)
    else:
        print(st.prod(a-1, b-1))
