from atcoder.segtree import SegTree

INF = 10 ** 18
N, K = map(int, input().split())
A = list(map(int, input().split()))
st = SegTree(max, -INF, N)
data = [0] * N
data[0] = A[0]
st.set(0, A[0])
for n in range(1, N):
    l = max(n - K, 0)
    m = st.prod(l, n)
    newVal = m + A[n]
    st.set(n, newVal)
    data[n] = newVal
print(data[-1])
