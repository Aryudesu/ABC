from atcoder.segtree import SegTree

INF = 10**18
N, K = map(int, input().split())
A = list(map(int, input().split()))
st = SegTree(min, INF, N)
st.set(0, A[0])
for idx in range(1, N):
    tmp = st.prod(max(0, idx - K), idx)
    st.set(idx, tmp + A[idx])
print(st.prod(N-1, N))
