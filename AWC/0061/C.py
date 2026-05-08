from atcoder.segtree import SegTree

INF = 10**18
N, K = map(int, input().split())
A = list(map(int, input().split()))
# とったときの最大値
st1 = SegTree(max, -INF, N)
st1.set(0, A[0])
for i in range(1, N):
    # 取ったときの最大値
    tmp1 = st1.prod(0, max(0, i - K + 1))
    st1.set(i, tmp1 + A[i])
print(st1.prod(0, N))
