from atcoder.fenwicktree import FenwickTree
from atcoder.lazysegtree import LazySegTree

MOD = 998244353
N, Q = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
AB = [A[i] * B[i] for i in range(N)]
ftAB = FenwickTree(N)
for n in range(N):
    ftAB.add(n, A[n] * B[n])
dataA = LazySegTree()
dataTA = [0] * N
dataB = [0] * N
dataTB = [0] * N
result = []
for q in range(Q):
    num, *query = [int(l) for l in input().split()]
    if num == 1:
        l, r, x = query
    elif num == 2:
        l, r, x = query
    elif num == 3:
        l, r = query
        tmp = ftAB.sum(l - 1, r)
        result.append(tmp)
    else:
        raise Exception()
print(result)
